# To run this code you need to install the following dependencies:
# pip install google-genai python-dotenv

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from tooling import ALL_TOOL_DECLARATIONS, TOOL_DISPATCH

DEFAULT_SYSTEM_PROMPT_PATH = os.path.join(os.path.dirname(__file__), "system_prompt.txt")


def load_system_prompt(prompt_path: str = DEFAULT_SYSTEM_PROMPT_PATH) -> str:
    """Loads system prompt from the specified file path."""
    if os.path.exists(prompt_path):
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception as e:
            print(f"Warning: Could not read system prompt file: {e}")
    return (
        "You are an intelligent, helpful College Administration Assistant with access "
        "to the college student database via function tools."
    )


def get_client() -> genai.Client:
    """Initializes and returns a Gemini client using API key from .env."""
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY / GEMINI_API_KEY is not set. Please add it to your .env file.")
    return genai.Client(api_key=api_key)


def create_chat_session(system_instruction: str = None, tools: list = None, model: str = "gemini-3.6-flash"):
    """
    Creates and returns a multi-turn chat session with function calling tools configured.
    Args:
        system_instruction: Optional system instruction prompt. If None, loaded from system_prompt.txt.
        tools: Optional list of tool functions. If None, ALL_TOOLS from tooling.py is used.
        model: The Gemini model name (defaults to 'gemini-3.6-flash').
    Returns:
        A tuple of (client, chat_session).
    """
    client = get_client()

    if system_instruction is None:
        system_instruction = load_system_prompt()

    # Wrap declarations into the types.Tool format the Gemini SDK expects
    tool_declarations = [
        types.Tool(function_declarations=[
            types.FunctionDeclaration(**decl) for decl in ALL_TOOL_DECLARATIONS
        ])
    ]

    if tools is None:
        tools = tool_declarations

    config = types.GenerateContentConfig(
        tools=tools,
        system_instruction=system_instruction,
        temperature=0.2,
        thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    )

    return client, config


def call_tool(fn_name: str, fn_args: dict):
    """Dispatch a function call to the matching tool in TOOL_DISPATCH."""
    fn = TOOL_DISPATCH.get(fn_name)
    if fn is None:
        return {"error": f"Unknown function: {fn_name}"}
    result = fn(**fn_args)
    return result if result is not None else {"result": "No data found."}


def chat_turn(client, history: list, user_input: str, config) -> str:
    """Send one user turn, execute any tool calls, and return the final text reply."""
    import json
    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    while True:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=history,
            config=config,
        )
        candidate = response.candidates[0]
        content = candidate.content
        history.append(content)

        # Collect any function-call parts
        fn_calls = [p for p in content.parts if p.function_call]
        if not fn_calls:
            # No more tool calls — collect and return text
            text_parts = [p.text for p in content.parts if p.text]
            return " ".join(text_parts).strip()

        # Execute each tool and feed results back to the model
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


def create_chatbot():
    """Runs the interactive terminal chatbot with function calling support."""
    # Ensure UTF-8 output encoding for terminal compatibility across platforms
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")

    try:
        client, config = create_chat_session()
    except Exception as e:
        print(f"Initialization Error: {e}")
        sys.exit(1)

    history = []  # Maintain conversation history for multi-turn context

    print("=" * 65)
    print("Gemini AI College Administration Assistant")
    print("Connected to college.db via tooling.py")
    print("Ask about students, marks, fees, courses, or stats.")
    print("Type 'quit', 'bye', or 'exit' to end the session.")
    print("=" * 65)

    exit_commands = {"quit", "bye", "exit"}

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in exit_commands:
                print("\nBot: Goodbye! Have a wonderful day!\n")
                break

            reply = chat_turn(client, history, user_input, config)
            print(f"\nBot: {reply}")

        except KeyboardInterrupt:
            print("\n\nBot: Session interrupted. Goodbye!\n")
            break
        except EOFError:
            print("\n\nBot: Exiting chat session. Goodbye!\n")
            break
        except Exception as e:
            print(f"\n[Error]: {e}")


if __name__ == "__main__":
    create_chatbot()
