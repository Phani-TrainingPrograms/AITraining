import os
import sys
import tkinter as tk
from tkinter import font as tkfont
from collections import deque
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------

# Ensure this script can find the project .env regardless of cwd
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_SCRIPT_DIR, ".env"))

# Short-term memory: keep last 3 (user, bot) conversation pairs
_MEMORY: deque = deque(maxlen=3)


# ---------------------------------------------------------------------------
# Gemini helpers
# ---------------------------------------------------------------------------

def _get_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "API key not found. "
            "Please set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file."
        )
    return genai.Client(api_key=api_key)


def _build_history_prompt(user_input: str) -> str:
    """Prepend the last few exchanges as context, then append the new query."""
    lines = []
    for u, b in _MEMORY:
        lines.append(f"User: {u}")
        lines.append(f"Bot: {b}")
    lines.append(f"User: {user_input}")
    return "\n".join(lines)


def query_bot(user_input: str) -> str:
    """Send the user input (with memory context) to Gemini and return the full response."""
    client = _get_client()
    model = "gemini-3.5-flash-lite"

    chat_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    )

    prompt = _build_history_prompt(user_input)

    # Collect streamed chunks
    response_parts = []
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=prompt,
        config=chat_config,
    ):
        if chunk.text:
            response_parts.append(chunk.text)

    bot_reply = "".join(response_parts).strip()

    # Store this turn in short-term memory
    _MEMORY.append((user_input, bot_reply))

    return bot_reply


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

class ChatApp(tk.Tk):
    """Tkinter chatbot UI."""

    TAG_USER = "user"
    TAG_BOT  = "bot"
    TAG_SEP  = "sep"

    def __init__(self):
        super().__init__()

        self.title("Gemini AI Chatbot")

        # Window sizing: half the screen
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w, h = sw // 2, sh // 2
        x, y = sw // 4, sh // 4
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.minsize(400, 300)

        # Fonts
        self._chat_font  = tkfont.Font(family="Segoe UI", size=11)
        self._entry_font = tkfont.Font(family="Segoe UI", size=11)
        self._btn_font   = tkfont.Font(family="Segoe UI", size=11, weight="bold")

        self._build_widgets()
        self._bind_keys()

    def _build_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=9)   # 90% - display area
        self.rowconfigure(1, weight=1)   # 10% - input row

        # ---- Display area (row 0) ----------------------------------------
        display_frame = tk.Frame(self, bg="#1e1e2e")
        display_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 4))
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(0, weight=1)

        self._chat_box = tk.Text(
            display_frame,
            state="disabled",
            wrap="word",
            bg="#1e1e2e",
            fg="#cdd6f4",
            font=self._chat_font,
            relief="flat",
            padx=10,
            pady=10,
            cursor="arrow",
            selectbackground="#313244",
        )
        self._chat_box.grid(row=0, column=0, sticky="nsew")

        scrollbar = tk.Scrollbar(display_frame, command=self._chat_box.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self._chat_box["yscrollcommand"] = scrollbar.set

        # Colour tags
        self._chat_box.tag_configure(
            self.TAG_USER,
            foreground="#f38ba8",
            font=tkfont.Font(family="Segoe UI", size=11, weight="bold"),
        )
        self._chat_box.tag_configure(
            self.TAG_BOT,
            foreground="#89b4fa",
        )
        self._chat_box.tag_configure(
            self.TAG_SEP,
            foreground="#45475a",
        )

        # ---- Input row (row 1) -------------------------------------------
        input_frame = tk.Frame(self, bg="#181825")
        input_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(4, 10))
        input_frame.columnconfigure(0, weight=1)
        input_frame.rowconfigure(0, weight=1)

        self._entry = tk.Entry(
            input_frame,
            font=self._entry_font,
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",
            relief="flat",
            bd=6,
        )
        self._entry.grid(row=0, column=0, sticky="nsew", padx=(0, 6))

        self._send_btn = tk.Button(
            input_frame,
            text="Send",
            font=self._btn_font,
            bg="#89b4fa",
            fg="#1e1e2e",
            activebackground="#b4befe",
            activeforeground="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self._on_send,
            padx=14,
        )
        self._send_btn.grid(row=0, column=1, sticky="nsew")

        self._entry.focus_set()

    def _bind_keys(self):
        self._entry.bind("<Return>", lambda _e: self._on_send())
        self._send_btn.bind("<Return>", lambda _e: self._on_send())

    def _append_text(self, label: str, text: str, tag: str):
        self._chat_box.configure(state="normal")
        self._chat_box.insert("end", f"{label} ", tag)
        self._chat_box.insert("end", f"{text}\n", tag)
        self._chat_box.configure(state="disabled")
        self._chat_box.see("end")

    def _append_separator(self):
        self._chat_box.configure(state="normal")
        self._chat_box.insert("end", "\n", self.TAG_SEP)
        self._chat_box.configure(state="disabled")

    def _on_send(self):
        user_input = self._entry.get().strip()
        if not user_input:
            return

        self._entry.delete(0, "end")
        self._append_text("You:", user_input, self.TAG_USER)

        self._send_btn.configure(state="disabled", text="...")
        self.update_idletasks()

        try:
            bot_reply = query_bot(user_input)
        except Exception as exc:
            bot_reply = f"[Error] {exc}"

        self._append_text("Bot:", bot_reply, self.TAG_BOT)
        self._append_separator()

        self._send_btn.configure(state="normal", text="Send")
        self._entry.focus_set()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if sys.stdout and sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    app = ChatApp()
    app.mainloop()
