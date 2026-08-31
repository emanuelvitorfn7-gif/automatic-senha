"""Interface gráfica do Analisador e Gerador de Senhas."""

import tkinter as tk
from tkinter import messagebox, ttk

from password_tools import analyze_password, generate_password


BACKGROUND = "#0d1117"
CARD = "#161b22"
CARD_LIGHT = "#21262d"
ENTRY_BACKGROUND = "#0d1117"
BORDER = "#30363d"
TEXT = "#f0f3f6"
MUTED_TEXT = "#9da7b3"
ACCENT = "#7c3aed"
ACCENT_ACTIVE = "#6d28d9"


class PasswordApp(tk.Tk):
    """Janela principal do aplicativo."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Analisador e Gerador de Senhas")
        self.geometry("720x570")
        self.minsize(650, 520)
        self.configure(bg=BACKGROUND)

        self._configure_styles()
        self._create_header()

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.analyzer_tab = ttk.Frame(notebook, padding=22)
        self.generator_tab = ttk.Frame(notebook, padding=22)
        notebook.add(self.analyzer_tab, text="  Analisar senha  ")
        notebook.add(self.generator_tab, text="  Gerar senha forte  ")

        self._build_analyzer_tab()
        self._build_generator_tab()

    def _configure_styles(self) -> None:
        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure("TFrame", background=CARD)
        style.configure("TLabel", background=CARD, foreground=TEXT)
        style.configure("Title.TLabel", font=("Segoe UI", 15, "bold"))
        style.configure("Subtitle.TLabel", font=("Segoe UI", 10), foreground=MUTED_TEXT)
        style.configure("Result.TLabel", font=("Segoe UI", 13, "bold"))
        style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8),
            background=ACCENT,
            foreground="#ffffff",
            bordercolor=ACCENT,
            focusthickness=1,
            focuscolor=ACCENT,
        )
        style.map(
            "TButton",
            background=[("pressed", ACCENT_ACTIVE), ("active", ACCENT_ACTIVE)],
            foreground=[("disabled", "#6e7681"), ("!disabled", "#ffffff")],
        )
        style.configure(
            "TCheckbutton",
            background=CARD,
            foreground=TEXT,
            font=("Segoe UI", 10),
            indicatorbackground=ENTRY_BACKGROUND,
            indicatorforeground=ACCENT,
        )
        style.map(
            "TCheckbutton",
            background=[("active", CARD)],
            foreground=[("active", TEXT)],
            indicatorbackground=[("selected", ACCENT), ("!selected", ENTRY_BACKGROUND)],
        )
        style.configure(
            "TEntry",
            fieldbackground=ENTRY_BACKGROUND,
            foreground=TEXT,
            insertcolor=TEXT,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            padding=5,
        )
        style.map(
            "TEntry",
            fieldbackground=[("readonly", ENTRY_BACKGROUND), ("focus", ENTRY_BACKGROUND)],
            foreground=[("readonly", TEXT)],
            bordercolor=[("focus", ACCENT)],
        )
        style.configure(
            "TSpinbox",
            fieldbackground=ENTRY_BACKGROUND,
            foreground=TEXT,
            arrowcolor=TEXT,
            bordercolor=BORDER,
            insertcolor=TEXT,
        )
        style.map(
            "TSpinbox",
            fieldbackground=[("focus", ENTRY_BACKGROUND)],
            bordercolor=[("focus", ACCENT)],
        )
        style.configure(
            "TNotebook",
            background=BACKGROUND,
            borderwidth=0,
            tabmargins=(0, 0, 0, 0),
        )
        style.configure(
            "TNotebook.Tab",
            background=CARD_LIGHT,
            foreground=MUTED_TEXT,
            padding=(18, 10),
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", ACCENT), ("active", "#30363d")],
            foreground=[("selected", "#ffffff"), ("active", TEXT)],
        )
        style.configure(
            "TLabelframe",
            background=CARD,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            relief="solid",
        )
        style.configure(
            "TLabelframe.Label",
            background=CARD,
            foreground=TEXT,
            font=("Segoe UI", 10, "bold"),
        )
        style.configure(
            "VeryWeak.Horizontal.TProgressbar",
            thickness=15,
            troughcolor=CARD_LIGHT,
            background="#ef4444",
            bordercolor=CARD_LIGHT,
        )
        style.configure(
            "Weak.Horizontal.TProgressbar",
            thickness=15,
            troughcolor=CARD_LIGHT,
            background="#f97316",
            bordercolor=CARD_LIGHT,
        )
        style.configure(
            "Medium.Horizontal.TProgressbar",
            thickness=15,
            troughcolor=CARD_LIGHT,
            background="#eab308",
            bordercolor=CARD_LIGHT,
        )
        style.configure(
            "Strong.Horizontal.TProgressbar",
            thickness=15,
            troughcolor=CARD_LIGHT,
            background="#22c55e",
            bordercolor=CARD_LIGHT,
        )
        style.configure(
            "VeryStrong.Horizontal.TProgressbar",
            thickness=15,
            troughcolor=CARD_LIGHT,
            background="#06b6d4",
            bordercolor=CARD_LIGHT,
        )

    def _create_header(self) -> None:
        header = tk.Frame(self, bg=BACKGROUND)
        header.pack(fill="x", padx=20, pady=18)

        tk.Label(
            header,
            text="Analisador e Gerador de Senhas",
            bg=BACKGROUND,
            fg=TEXT,
            font=("Segoe UI", 19, "bold"),
        ).pack(anchor="w")
        tk.Label(
            header,
            text="Analise sua senha em tempo real ou crie uma senha segura.",
            bg=BACKGROUND,
            fg=MUTED_TEXT,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(3, 0))

    def _build_analyzer_tab(self) -> None:
        ttk.Label(self.analyzer_tab, text="Digite uma senha", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            self.analyzer_tab,
            text="A análise acontece automaticamente a cada caractere digitado.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(3, 10))

        input_row = ttk.Frame(self.analyzer_tab)
        input_row.pack(fill="x")
        input_row.columnconfigure(0, weight=1)

        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            input_row,
            textvariable=self.password_var,
            show="•",
            font=("Segoe UI", 12),
        )
        self.password_entry.grid(row=0, column=0, sticky="ew", ipady=7)

        self.show_analyzed_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            input_row,
            text="Mostrar",
            variable=self.show_analyzed_var,
            command=self._toggle_analyzed_password,
        ).grid(row=0, column=1, padx=(10, 0))

        self.strength_label = ttk.Label(
            self.analyzer_tab,
            text="Força: digite uma senha",
            style="Result.TLabel",
        )
        self.strength_label.pack(anchor="w", pady=(18, 8))

        self.strength_bar = ttk.Progressbar(
            self.analyzer_tab,
            maximum=100,
            value=0,
            mode="determinate",
            style="VeryWeak.Horizontal.TProgressbar",
        )
        self.strength_bar.pack(fill="x")

        ttk.Label(self.analyzer_tab, text="O que falta para ficar forte:", style="Title.TLabel").pack(
            anchor="w", pady=(20, 7)
        )
        self.feedback_label = ttk.Label(
            self.analyzer_tab,
            text="• Comece a digitar para receber sugestões.",
            justify="left",
            wraplength=620,
        )
        self.feedback_label.pack(anchor="w", fill="x")

        suggestion_box = ttk.LabelFrame(self.analyzer_tab, text=" Sugestão automática mais forte ", padding=12)
        suggestion_box.pack(fill="x", pady=(20, 0))
        suggestion_box.columnconfigure(0, weight=1)

        self.suggestion_var = tk.StringVar(value="Digite uma senha para gerar uma sugestão.")
        self.suggestion_entry = ttk.Entry(
            suggestion_box,
            textvariable=self.suggestion_var,
            state="readonly",
            font=("Consolas", 11),
        )
        self.suggestion_entry.grid(row=0, column=0, sticky="ew", ipady=6)
        ttk.Button(
            suggestion_box,
            text="Copiar",
            command=lambda: self._copy_to_clipboard(self.suggestion_var.get()),
        ).grid(row=0, column=1, padx=(10, 0))

        self.password_var.trace_add("write", self._update_analysis)
        self.password_entry.focus_set()

    def _build_generator_tab(self) -> None:
        ttk.Label(self.generator_tab, text="Configurar nova senha", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            self.generator_tab,
            text="Escolha o tamanho e os tipos de caracteres desejados.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(3, 16))

        length_frame = ttk.Frame(self.generator_tab)
        length_frame.pack(fill="x")
        ttk.Label(length_frame, text="Quantidade de caracteres (6 a 128):").pack(side="left")
        self.length_var = tk.IntVar(value=18)
        ttk.Spinbox(
            length_frame,
            from_=6,
            to=128,
            textvariable=self.length_var,
            width=7,
            justify="center",
        ).pack(side="left", padx=10)

        options = ttk.LabelFrame(self.generator_tab, text=" Opções ", padding=12)
        options.pack(fill="x", pady=18)

        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.ambiguous_var = tk.BooleanVar(value=True)

        option_items = (
            ("Maiúsculas (A-Z)", self.upper_var),
            ("Minúsculas (a-z)", self.lower_var),
            ("Numerais (0-9)", self.digits_var),
            ("Caracteres especiais (!@#$...)", self.special_var),
            ("Evitar caracteres ambíguos (I, l, 1, O, 0, o)", self.ambiguous_var),
        )
        for row, (text, variable) in enumerate(option_items):
            ttk.Checkbutton(options, text=text, variable=variable).grid(row=row, column=0, sticky="w", pady=3)

        ttk.Button(
            self.generator_tab,
            text="Gerar senha forte",
            command=self._generate_configured_password,
        ).pack(anchor="w")

        result_box = ttk.LabelFrame(self.generator_tab, text=" Senha gerada ", padding=12)
        result_box.pack(fill="x", pady=(20, 0))
        result_box.columnconfigure(0, weight=1)

        self.generated_var = tk.StringVar()
        self.generated_entry = ttk.Entry(
            result_box,
            textvariable=self.generated_var,
            state="readonly",
            font=("Consolas", 12),
        )
        self.generated_entry.grid(row=0, column=0, sticky="ew", ipady=7)
        ttk.Button(
            result_box,
            text="Copiar",
            command=lambda: self._copy_to_clipboard(self.generated_var.get()),
        ).grid(row=0, column=1, padx=(10, 0))

        self.generated_info = ttk.Label(
            self.generator_tab,
            text="",
            style="Subtitle.TLabel",
        )
        self.generated_info.pack(anchor="w", pady=(8, 0))

        self._generate_configured_password()

    def _toggle_analyzed_password(self) -> None:
        self.password_entry.configure(show="" if self.show_analyzed_var.get() else "•")

    def _update_analysis(self, *_args: object) -> None:
        password = self.password_var.get()
        result = analyze_password(password)

        progress_styles = {
            "Muito fraca": "VeryWeak.Horizontal.TProgressbar",
            "Fraca": "Weak.Horizontal.TProgressbar",
            "Intermediária": "Medium.Horizontal.TProgressbar",
            "Forte": "Strong.Horizontal.TProgressbar",
            "Muito forte": "VeryStrong.Horizontal.TProgressbar",
        }
        self.strength_bar.configure(style=progress_styles[result["level"]])

        self.strength_label.configure(
            text=f"Força: {result['level']} — {result['percentage']}%"
        )
        self.strength_bar["value"] = result["percentage"]

        if password:
            feedback = result["feedback"] or ["Excelente: a senha atende a todos os critérios."]
            self.feedback_label.configure(text="\n".join(f"• {item}" for item in feedback))

            suggestion_length = max(16, min(24, len(password) + 4))
            self.suggestion_var.set(generate_password(length=suggestion_length))
        else:
            self.strength_label.configure(text="Força: digite uma senha")
            self.strength_bar["value"] = 0
            self.feedback_label.configure(text="• Comece a digitar para receber sugestões.")
            self.suggestion_var.set("Digite uma senha para gerar uma sugestão.")

    def _generate_configured_password(self) -> None:
        try:
            length = int(self.length_var.get())
            password = generate_password(
                length=length,
                use_upper=self.upper_var.get(),
                use_lower=self.lower_var.get(),
                use_digits=self.digits_var.get(),
                use_special=self.special_var.get(),
                avoid_ambiguous=self.ambiguous_var.get(),
            )
        except (ValueError, tk.TclError) as error:
            messagebox.showerror("Não foi possível gerar", str(error))
            return

        self.generated_var.set(password)
        result = analyze_password(password)
        self.generated_info.configure(text=f"Força estimada: {result['level']} ({result['percentage']}%)")

    def _copy_to_clipboard(self, text: str) -> None:
        if not text or text.startswith("Digite uma senha"):
            messagebox.showinfo("Copiar", "Ainda não há uma senha para copiar.")
            return

        self.clipboard_clear()
        self.clipboard_append(text)
        self.update_idletasks()
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência.")


if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()
