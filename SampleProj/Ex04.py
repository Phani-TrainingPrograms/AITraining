import json
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tooling import ALL_TOOL_DECLARATIONS, TOOL_DISPATCH

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_SCRIPT_DIR, ".env"))

_SYSTEM_PROMPT_PATH = os.path.join(_SCRIPT_DIR, "system_prompt.txt")
MODEL = "gemini-3.5-flash-lite"


def load_system_prompt():
    with open(_SYSTEM_PROMPT_PATH, encoding="utf-8") as f:
        return f.read().strip()


def get_client():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: API Key not found. Set GOOGLE_API_KEY in .env")
        sys.exit(1)
    return genai.Client(api_key=api_key)


def call_tool(fn_name, fn_args):
    fn = TOOL_DISPATCH.get(fn_name)
    if fn is None:
        return {"error": f"Unknown function: {fn_name}"}
    result = fn(**fn_args)
    return result if result is not None else {"result": "No data found."}


def chat_turn(client, history, user_input, system_prompt):
    """Send one user turn with function-calling support. Returns bot reply string."""
    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    tool_declarations = [
        types.Tool(function_declarations=[
            types.FunctionDeclaration(**decl) for decl in ALL_TOOL_DECLARATIONS
        ])
    ]

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=tool_declarations,
        thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    )

    while True:
        response = client.models.generate_content(
            model=MODEL,
            contents=history,
            config=config,
        )
        candidate = response.candidates[0]
        content = candidate.content
        history.append(content)

        # Check for function calls
        fn_calls = [p for p in content.parts if p.function_call]
        if not fn_calls:
            # Final text response
            text_parts = [p.text for p in content.parts if p.text]
            return " ".join(text_parts).strip()

        # Execute each function call and return results
        fn_results = []
        for part in fn_calls:
            fc = part.function_call
            result = call_tool(fc.name, dict(fc.args))
            fn_results.append(
                types.Part(
                    function_response=types.FunctionResponse(
                        name=fc.name,
                        response={"result": json.dumps(result, ensure_ascii=False)},
                    )
                )
            )
        history.append(types.Content(role="user", parts=fn_results))


def start_chat():
    client = get_client()
    system_prompt = load_system_prompt()
    history = []
    exit_keywords = {"quit", "bye", "exit"}

    print("=" * 60)
    print("Grocery Store Assistant (Ex04) - Function Calling Demo")
    print("Ask about fruits, vegetables, prices, or the full menu.")
    print("Type quit / bye / exit to end.")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() in exit_keywords:
                print("\nBot: Goodbye! Happy shopping!")
                break

            reply = chat_turn(client, history, user_input, system_prompt)
            print(f"\nBot: {reply}")

        except KeyboardInterrupt:
            print("\n\nBot: Interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n[Error]: {e}")


if __name__ == "__main__":
    start_chat()
