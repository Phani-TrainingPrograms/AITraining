import json
import os
import sys
import tkinter as tk
from tkinter import font as tkfont, messagebox
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ── Bootstrap ────────────────────────────────────────────────────────────────

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_SCRIPT_DIR, ".env"))

_SYSTEM_PROMPT_PATH = os.path.join(_SCRIPT_DIR, "system_prompt.txt")
MODEL = "gemini-3.5-flash-lite"

# ── Lazy import of tooling ───────────────────────────────────────────────────
try:
    from tooling import ALL_TOOL_DECLARATIONS, TOOL_DISPATCH
    _TOOLING_AVAILABLE = True
except ImportError:
    _TOOLING_AVAILABLE = False
    ALL_TOOL_DECLARATIONS = []
    TOOL_DISPATCH = {}

# ── State ────────────────────────────────────────────────────────────────────

_history = []          # list of genai.types.Content
_system_prompt = None  # str or None


# ── Gemini helpers ───────────────────────────────────────────────────────────

def _get_client():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "API key not found. Set GOOGLE_API_KEY in .env"
        )
    return genai.Client(api_key=api_key)


def _call_tool(fn_name, fn_args):
    fn = TOOL_DISPATCH.get(fn_name)
    if fn is None:
        return {"error": f"Unknown function: {fn_name}"}
    result = fn(**fn_args)
    return result if result is not None else {"result": "No data found."}


def query_bot(user_input: str) -> str:
    global _history, _system_prompt

    client = _get_client()

    _history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    config_kwargs = {}
    if _system_prompt:
        config_kwargs["system_instruction"] = _system_prompt

    if _TOOLING_AVAILABLE and _system_prompt:
        tool_declarations = [
            types.Tool(function_declarations=[
                types.FunctionDeclaration(**decl) for decl in ALL_TOOL_DECLARATIONS
            ])
        ]
        config_kwargs["tools"] = tool_declarations

    config_kwargs["thinking_config"] = types.ThinkingConfig(thinking_level="MINIMAL")
    config = types.GenerateContentConfig(**config_kwargs)

    while True:
        response = client.models.generate_content(
            model=MODEL,
            contents=_history,
            config=config,
        )
        candidate = response.candidates[0]
        content = candidate.content
        _history.append(content)

        fn_calls = [p for p in content.parts if p.function_call]
        if not fn_calls:
            text_parts = [p.text for p in content.parts if p.text]
            return " ".join(text_parts).strip()

        fn_results = []
        for part in fn_calls:
            fc = part.function_call
            result = _call_tool(fc.name, dict(fc.args))
            fn_results.append(
                types.Part(
                    function_response=types.FunctionResponse(
                        name=fc.name,
                        response={"result": json.dumps(result, ensure_ascii=False)},
                    )
                )
            )
        _history.append(types.Content(role="user", parts=fn_results))


# ── ChatApp UI ───────────────────────────────────────────────────────────────

class ChatApp(tk.Tk):
    TAG_USER = "user"
    TAG_BOT  = "bot"
    TAG_SEP  = "sep"
    TAG_SYS  = "sys"

    def __init__(self):
        super().__init__()
        self.title("Gemini AI Chatbot")

        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w, h = sw // 2, sh // 2
        x, y = sw // 4, sh // 4
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.minsize(400, 300)

        self._chat_font  = tkfont.Font(family="Segoe UI", size=11)
        self._entry_font = tkfont.Font(family="Segoe UI", size=11)
        self._btn_font   = tkfont.Font(family="Segoe UI", size=11, weight="bold")
        self._small_font = tkfont.Font(family="Segoe UI", size=9)

        self._build_widgets()
        self._bind_keys()

    def _build_widgets(self):
        self.configure(bg="#181825")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)   # toolbar
        self.rowconfigure(1, weight=9)   # 90% display
        self.rowconfigure(2, weight=1)   # 10% input

        # ── Toolbar (row 0) ───────────────────────────────────────────────
        toolbar = tk.Frame(self, bg="#11111b", pady=4)
        toolbar.grid(row=0, column=0, sticky="ew", padx=10, pady=(8, 0))
        toolbar.columnconfigure(0, weight=1)

        self._load_btn = tk.Button(
            toolbar,
            text="⚙ Load System Prompt",
            font=self._small_font,
            bg="#313244",
            fg="#cba6f7",
            activebackground="#45475a",
            activeforeground="#cba6f7",
            relief="flat",
            cursor="hand2",
            command=self._on_load_system_prompt,
            padx=10,
            pady=3,
        )
        self._load_btn.pack(side="left")

        self._status_lbl = tk.Label(
            toolbar,
            text="No system prompt loaded",
            font=self._small_font,
            bg="#11111b",
            fg="#6c7086",
        )
        self._status_lbl.pack(side="left", padx=12)

        # ── Display area (row 1) ──────────────────────────────────────────
        display_frame = tk.Frame(self, bg="#1e1e2e")
        display_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(6, 4))
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

        self._chat_box.tag_configure(
            self.TAG_USER,
            foreground="#f38ba8",
            font=tkfont.Font(family="Segoe UI", size=11, weight="bold"),
        )
        self._chat_box.tag_configure(self.TAG_BOT, foreground="#89b4fa")
        self._chat_box.tag_configure(self.TAG_SEP, foreground="#45475a")
        self._chat_box.tag_configure(
            self.TAG_SYS,
            foreground="#a6e3a1",
            font=tkfont.Font(family="Segoe UI", size=9, slant="italic"),
        )

        # ── Input row (row 2) ─────────────────────────────────────────────
        input_frame = tk.Frame(self, bg="#181825")
        input_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(4, 10))
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

    def _clear_chat(self):
        self._chat_box.configure(state="normal")
        self._chat_box.delete("1.0", "end")
        self._chat_box.configure(state="disabled")

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

    def _on_load_system_prompt(self):
        global _history, _system_prompt
        if not os.path.exists(_SYSTEM_PROMPT_PATH):
            messagebox.showerror(
                "File Not Found",
                f"system_prompt.txt not found at:\n{_SYSTEM_PROMPT_PATH}",
            )
            return

        with open(_SYSTEM_PROMPT_PATH, encoding="utf-8") as f:
            _system_prompt = f.read().strip()

        # Reset conversation history
        _history = []

        # Clear the chat display
        self._clear_chat()

        # Update toolbar status
        self._status_lbl.configure(
            text="System prompt loaded  |  History cleared", fg="#a6e3a1"
        )

        # Show confirmation in chat
        self._append_text(
            "System:",
            "System prompt loaded. Conversation history has been reset.",
            self.TAG_SYS,
        )
        self._append_separator()

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


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if sys.stdout and sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    app = ChatApp()
    app.mainloop()
