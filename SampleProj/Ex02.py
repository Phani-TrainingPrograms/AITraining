import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Ensure proper encoding on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Load environment variables from .env file
load_dotenv()


def start_chat():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: API Key not found!")
        print("Please ensure GOOGLE_API_KEY is set in your .env file.")
        sys.exit(1)

    # Initialize Gemini client with API key from .env
    client = genai.Client(api_key=api_key)

    # Model and chat configuration
    model = "gemini-3.5-flash-lite"
    chat_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="MINIMAL",
        ),
    )

    # Initialize multi-turn chat session
    chat = client.chats.create(
        model=model,
        config=chat_config,
    )

    print("=" * 60)
    print("Welcome to the Gemini AI Chatbot!")
    print("Type your questions below.")
    print("To end the conversation, type 'quit', 'bye', or 'exit'.")
    print("=" * 60)

    # Exit keywords defined in prompt
    exit_keywords = {"quit", "bye", "exit"}

    while True:
        try:
            user_input = input("\nYou: ").strip()

            # Skip empty inputs
            if not user_input:
                continue

            # Check for exit command
            if user_input.lower() in exit_keywords:
                print("\nBot: Goodbye! Have a wonderful day!\n")
                break

            print("\nBot: ", end="", flush=True)

            # Stream response in real-time
            for chunk in chat.send_message_stream(user_input):
                if text := chunk.text:
                    print(text, end="", flush=True)
            print()

        except KeyboardInterrupt:
            print("\n\nBot: Chat interrupted. Goodbye!\n")
            break
        except EOFError:
            print("\n\nBot: Input closed. Goodbye!\n")
            break
        except Exception as e:
            print(f"\n[Error]: {e}")


if __name__ == "__main__":
    start_chat()
