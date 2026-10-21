import json
import os
import tkinter as tk
from tkinter import filedialog, font as tkfont, messagebox, ttk

from PIL import Image, ImageTk

# Dark colour scheme shared by the ttk styles, the tk widgets and the canvas
BG = "#16181d"
SURFACE = "#1e2128"
SURFACE_ALT = "#262a33"
BORDER = "#323743"
TEXT = "#e6e8ee"
MUTED = "#8b93a5"
ACCENT = "#5b8cff"
ACCENT_HOVER = "#7aa2ff"
CANVAS_BG = "#101216"

# Each part gets its own colour, used for its box on the image and its entry in the parts list
PART_COLOURS = ["#4ade80", "#60a5fa", "#f472b6", "#facc15", "#a78bfa", "#fb923c", "#2dd4bf"]


class PartsViewer(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Question Parts Viewer")
        self.geometry("1280x900")
        self.minsize(900, 600)
        self.configure(bg=BG)

        self.data = []
        self.images_dir = ""
        self.current_index = 0
        self.current_image = None
        self.current_photo = None
        self.current_scale = 1.0
        self.current_offset = (0, 0)
        self.zoom_factor = 1.0
        self.min_zoom = 0.2
        self.max_zoom = 5.0
        self.pan_offset = (0, 0)
        self.drag_start = None

        self._build_fonts()
        self._build_styles()
        self._build_ui()
        self._bind_keys()

    def _build_fonts(self) -> None:
        base = tkfont.nametofont("TkDefaultFont").actual()["family"]
        self.font_body = tkfont.Font(family=base, size=10)
        self.font_bold = tkfont.Font(family=base, size=10, weight="bold")
        self.font_title = tkfont.Font(family=base, size=15, weight="bold")
        self.font_heading = tkfont.Font(family=base, size=9, weight="bold")
        mono = tkfont.nametofont("TkFixedFont").actual()["family"]
        self.font_mono = tkfont.Font(family=mono, size=9)

    def _build_styles(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(".", background=BG, foreground=TEXT, font=self.font_body,
                        bordercolor=BORDER, lightcolor=BORDER, darkcolor=BORDER)
        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=SURFACE, relief=tk.FLAT)
        style.configure("TLabel", background=BG, foreground=TEXT)
        style.configure("Card.TLabel", background=SURFACE, foreground=MUTED)
        style.configure("Title.TLabel", background=BG, foreground=TEXT, font=self.font_title)
        style.configure("Subtitle.TLabel", background=BG, foreground=MUTED)
        style.configure("Heading.TLabel", background=SURFACE, foreground=MUTED, font=self.font_heading)
        style.configure("Status.TLabel", background=SURFACE, foreground=MUTED, padding=(12, 6))

        style.configure("TEntry", fieldbackground=SURFACE_ALT, foreground=TEXT, insertcolor=TEXT,
                        bordercolor=BORDER, lightcolor=SURFACE_ALT, darkcolor=SURFACE_ALT, padding=6)
        style.map("TEntry", bordercolor=[("focus", ACCENT)], lightcolor=[("focus", ACCENT)])

        style.configure("TButton", background=SURFACE_ALT, foreground=TEXT, borderwidth=0,
                        focusthickness=0, padding=(12, 6))
        style.map("TButton", background=[("pressed", BORDER), ("active", BORDER)])
        style.configure("Accent.TButton", background=ACCENT, foreground="#ffffff", font=self.font_bold)
        style.map("Accent.TButton", background=[("pressed", ACCENT), ("active", ACCENT_HOVER)])

        style.configure("Vertical.TScrollbar", background=SURFACE_ALT, troughcolor=SURFACE,
                        bordercolor=SURFACE, arrowcolor=MUTED, lightcolor=SURFACE_ALT, darkcolor=SURFACE_ALT)

    def _build_ui(self) -> None:
        header = ttk.Frame(self, padding=(16, 14, 16, 6))
        header.pack(side=tk.TOP, fill=tk.X)
        ttk.Label(header, text="Question Parts Viewer", style="Title.TLabel").pack(side=tk.LEFT)
        ttk.Label(
            header,
            text="←/→ navigate   +/− zoom   0 reset   drag to pan",
            style="Subtitle.TLabel",
        ).pack(side=tk.RIGHT)

        controls = ttk.Frame(self, padding=(16, 10), style="Card.TFrame")
        controls.pack(side=tk.TOP, fill=tk.X, padx=16, pady=(0, 10))
        controls.columnconfigure(1, weight=3)
        controls.columnconfigure(4, weight=2)

        ttk.Label(controls, text="JSON", style="Card.TLabel").grid(row=0, column=0, sticky=tk.W)
        self.json_entry = ttk.Entry(controls, width=60)
        self.json_entry.grid(row=0, column=1, sticky=tk.EW, padx=(8, 6))
        ttk.Button(controls, text="Browse…", command=self._browse_json).grid(row=0, column=2)

        ttk.Label(controls, text="Images", style="Card.TLabel").grid(row=0, column=3, sticky=tk.W, padx=(18, 0))
        self.images_entry = ttk.Entry(controls, width=40)
        self.images_entry.grid(row=0, column=4, sticky=tk.EW, padx=(8, 6))
        ttk.Button(controls, text="Browse…", command=self._browse_images).grid(row=0, column=5)

        ttk.Button(controls, text="Load", style="Accent.TButton", command=self._load_data).grid(
            row=0, column=6, padx=(14, 0)
        )

        content = ttk.Frame(self)
        content.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=16, pady=(0, 10))

        right = ttk.Frame(content)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

        left = ttk.Frame(content, style="Card.TFrame")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(left, bg=CANVAS_BG, highlightthickness=0, cursor="fleur")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=1, pady=1)
        self.canvas.bind("<Configure>", self._on_canvas_resize)
        self.canvas.bind("<ButtonPress-1>", self._start_pan)
        self.canvas.bind("<B1-Motion>", self._pan)

        nav = ttk.Frame(left, padding=10, style="Card.TFrame")
        nav.pack(side=tk.BOTTOM, fill=tk.X)
        ttk.Button(nav, text="‹ Prev", command=self._prev_question).pack(side=tk.LEFT)
        ttk.Button(nav, text="Next ›", command=self._next_question).pack(side=tk.LEFT, padx=(6, 18))
        ttk.Button(nav, text="−", width=3, command=self._zoom_out).pack(side=tk.LEFT)
        self.zoom_label = ttk.Label(nav, text="100%", width=6, anchor=tk.CENTER, style="Card.TLabel")
        self.zoom_label.pack(side=tk.LEFT, padx=4)
        ttk.Button(nav, text="+", width=3, command=self._zoom_in).pack(side=tk.LEFT)
        ttk.Button(nav, text="Reset Zoom", command=self._reset_zoom).pack(side=tk.LEFT, padx=6)

        self.listbox = self._card_listbox(right, "QUESTIONS", height=12)
        self.listbox.bind("<<ListboxSelect>>", self._on_listbox_select)

        self.meta_text = self._card_text(right, "METADATA", height=8)
        self.meta_text.tag_configure("key", foreground=MUTED)
        self.meta_text.tag_configure("value", foreground=TEXT)

        self.question_text = self._card_text(right, "QUESTION TEXT", height=12)

        self.parts_text = self._card_text(right, "PARTS", height=14, expand=True)
        self.parts_text.tag_configure("index", foreground=MUTED)
        self.parts_text.tag_configure("coords", foreground=MUTED, font=self.font_mono)
        self.parts_text.tag_configure("empty", foreground=MUTED)
        for colour in PART_COLOURS:
            self.parts_text.tag_configure(colour, foreground=colour, font=self.font_bold)

        self.status_label = ttk.Label(self, text="No data loaded", style="Status.TLabel")
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X, before=content)

    def _card(self, parent: tk.Widget, title: str, expand: bool) -> ttk.Frame:
        card = ttk.Frame(parent, padding=(12, 10), style="Card.TFrame")
        card.pack(side=tk.TOP, fill=tk.BOTH, expand=expand, pady=(0, 10) if not expand else 0)
        ttk.Label(card, text=title, style="Heading.TLabel").pack(anchor=tk.W, pady=(0, 6))
        return card

    def _card_listbox(self, parent: tk.Widget, title: str, height: int) -> tk.Listbox:
        card = self._card(parent, title, expand=False)
        body = ttk.Frame(card, style="Card.TFrame")
        body.pack(fill=tk.X)
        listbox = tk.Listbox(
            body, height=height, width=42, bg=SURFACE_ALT, fg=TEXT, selectbackground=ACCENT,
            selectforeground="#ffffff", highlightthickness=0, borderwidth=0,
            activestyle="none", font=self.font_body,
        )
        scrollbar = ttk.Scrollbar(body, orient=tk.VERTICAL, command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        return listbox

    def _card_text(self, parent: tk.Widget, title: str, height: int, expand: bool = False) -> tk.Text:
        card = self._card(parent, title, expand=expand)
        body = ttk.Frame(card, style="Card.TFrame")
        body.pack(fill=tk.BOTH, expand=True)
        text = tk.Text(
            body, height=height, width=42, wrap=tk.WORD, bg=SURFACE_ALT, fg=TEXT, insertbackground=TEXT,
            highlightthickness=0, borderwidth=0, padx=8, pady=6, font=self.font_body,
            selectbackground=ACCENT, spacing1=1, spacing3=1,
        )
        scrollbar = ttk.Scrollbar(body, orient=tk.VERTICAL, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set, state=tk.DISABLED)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        return text

    def _bind_keys(self) -> None:
        self.bind("<Left>", lambda _event: self._prev_question())
        self.bind("<Right>", lambda _event: self._next_question())
        self.bind("<Up>", lambda _event: self._prev_question())
        self.bind("<Down>", lambda _event: self._next_question())
        self.bind("<Prior>", lambda _event: self._prev_question())
        self.bind("<Next>", lambda _event: self._next_question())
        self.bind("<plus>", lambda _event: self._zoom_in())
        self.bind("<minus>", lambda _event: self._zoom_out())
        self.bind("<Key-0>", lambda _event: self._reset_zoom())
        self.bind("<MouseWheel>", self._on_mousewheel)
        self.bind("<Button-4>", self._on_mousewheel)
        self.bind("<Button-5>", self._on_mousewheel)

    def _browse_json(self) -> None:
        path = filedialog.askopenfilename(
            title="Select questions_updated.json",
            filetypes=[("JSON files", "*.json"), ("All files", "*")],
        )
        if path:
            self.json_entry.delete(0, tk.END)
            self.json_entry.insert(0, path)

    def _browse_images(self) -> None:
        path = filedialog.askdirectory(title="Select images folder")
        if path:
            self.images_entry.delete(0, tk.END)
            self.images_entry.insert(0, path)

    def _load_data(self) -> None:
        json_path = self.json_entry.get().strip()
        images_dir = self.images_entry.get().strip()

        if not json_path or not os.path.isfile(json_path):
            messagebox.showerror("Invalid JSON", "Please select a JSON file.")
            return

        if not images_dir or not os.path.isdir(images_dir):
            messagebox.showerror("Invalid folder", "Please select an images folder.")
            return

        try:
            with open(json_path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            messagebox.showerror("Load error", f"Failed to read JSON: {exc}")
            return

        if not isinstance(data, list):
            messagebox.showerror(
                "Invalid format", "Expected a list of questions in the JSON file."
            )
            return

        self.data = data
        self.images_dir = images_dir
        self.current_index = 0
        self._populate_listbox()
        self._show_question(0)

    def _populate_listbox(self) -> None:
        self.listbox.delete(0, tk.END)
        for question in self.data:
            name = question.get("questionName", "(no name)")
            number = question.get("questionNum", "?")
            self.listbox.insert(tk.END, f"  Q{number}   {name}")

    def _on_listbox_select(self, _event: tk.Event) -> None:
        selection = self.listbox.curselection()
        if not selection:
            return
        index = int(selection[0])
        self._show_question(index)

    def _prev_question(self) -> None:
        if not self.data:
            return
        self._show_question((self.current_index - 1) % len(self.data))

    def _next_question(self) -> None:
        if not self.data:
            return
        self._show_question((self.current_index + 1) % len(self.data))

    def _show_question(self, index: int) -> None:
        if not self.data:
            return
        index = max(0, min(index, len(self.data) - 1))
        self.current_index = index
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(index)
        self.listbox.activate(index)
        self.listbox.see(index)
        question = self.data[index]

        self._update_question_text(question)
        self._load_image(question)
        self._reset_zoom()
        self._render_image()

        name = question.get("questionName", "(no name)")
        parts = len(question.get("questionParts", []))
        self.status_label.configure(
            text=f"{index + 1} / {len(self.data)}   ·   {name}   ·   {parts} part{'s' if parts != 1 else ''}"
        )

    def _update_question_text(self, question: dict) -> None:
        self.meta_text.configure(state=tk.NORMAL)
        self.meta_text.delete("1.0", tk.END)
        for key in sorted(question.keys()):
            if key in {"questionText", "questionParts"}:
                continue
            value = question.get(key)
            self.meta_text.insert(tk.END, f"{key}: ", "key")
            self.meta_text.insert(tk.END, f"{value}\n", "value")
        self.meta_text.configure(state=tk.DISABLED)

        text = question.get("questionText", "")
        self.question_text.configure(state=tk.NORMAL)
        self.question_text.delete("1.0", tk.END)
        self.question_text.insert(tk.END, text)
        self.question_text.configure(state=tk.DISABLED)

        parts = question.get("questionParts", [])
        self.parts_text.configure(state=tk.NORMAL)
        self.parts_text.delete("1.0", tk.END)
        if parts:
            for idx, part in enumerate(parts, start=1):
                coords = part.get("coordinates", [])
                label = part.get("text", "")
                colour = PART_COLOURS[(idx - 1) % len(PART_COLOURS)]
                self.parts_text.insert(tk.END, f"{idx:>2}  ", "index")
                self.parts_text.insert(tk.END, "■ ", colour)
                self.parts_text.insert(tk.END, f"{label}  ", colour)
                self.parts_text.insert(tk.END, f"{coords}\n", "coords")
        else:
            self.parts_text.insert(tk.END, "No parts found.", "empty")
        self.parts_text.configure(state=tk.DISABLED)

    def _load_image(self, question: dict) -> None:
        name = question.get("questionName", "")
        if not name:
            self.current_image = None
            return

        image_path = os.path.join(self.images_dir, name)
        if not os.path.isfile(image_path):
            self.current_image = None
            messagebox.showwarning("Missing image", f"Image not found: {image_path}")
            return

        try:
            self.current_image = Image.open(image_path)
        except OSError as exc:
            messagebox.showerror("Image error", f"Failed to open image: {exc}")
            self.current_image = None

    def _on_canvas_resize(self, _event: tk.Event) -> None:
        self._render_image()

    def _zoom_in(self) -> None:
        self._set_zoom(self.zoom_factor * 1.2)

    def _zoom_out(self) -> None:
        self._set_zoom(self.zoom_factor / 1.2)

    def _reset_zoom(self) -> None:
        self.pan_offset = (0, 0)
        self._set_zoom(1.0)

    def _set_zoom(self, value: float) -> None:
        self.zoom_factor = max(self.min_zoom, min(self.max_zoom, value))
        self.zoom_label.configure(text=f"{self.zoom_factor:.0%}")
        self._render_image()

    def _on_mousewheel(self, event: tk.Event) -> None:
        if hasattr(event, "delta") and event.delta != 0:
            if event.delta > 0:
                self._zoom_in()
            else:
                self._zoom_out()
            return

        if getattr(event, "num", None) == 4:
            self._zoom_in()
        elif getattr(event, "num", None) == 5:
            self._zoom_out()

    def _start_pan(self, event: tk.Event) -> None:
        self.drag_start = (event.x, event.y)

    def _pan(self, event: tk.Event) -> None:
        if self.drag_start is None:
            return
        start_x, start_y = self.drag_start
        dx = event.x - start_x
        dy = event.y - start_y
        current_x, current_y = self.pan_offset
        self.pan_offset = (current_x + dx, current_y + dy)
        self.drag_start = (event.x, event.y)
        self._render_image()

    def _render_image(self) -> None:
        self.canvas.delete("all")
        canvas_width = max(self.canvas.winfo_width(), 1)
        canvas_height = max(self.canvas.winfo_height(), 1)
        if self.current_image is None:
            message = "No image loaded" if self.data else "Choose a JSON file and images folder, then press Load"
            self.canvas.create_text(
                canvas_width // 2,
                canvas_height // 2,
                fill=MUTED,
                font=self.font_body,
                text=message,
            )
            return

        image_width, image_height = self.current_image.size

        scale = (
            min(
                canvas_width / image_width,
                canvas_height / image_height,
            )
            * self.zoom_factor
        )
        scaled_width = max(int(image_width * scale), 1)
        scaled_height = max(int(image_height * scale), 1)
        offset_x = (canvas_width - scaled_width) // 2
        offset_y = (canvas_height - scaled_height) // 2
        if offset_x < 0:
            offset_x = 0
        if offset_y < 0:
            offset_y = 0
        pan_x, pan_y = self.pan_offset
        offset_x += pan_x
        offset_y += pan_y

        resized = self.current_image.resize((scaled_width, scaled_height), Image.LANCZOS)
        self.current_photo = ImageTk.PhotoImage(resized)

        self.current_scale = scale
        self.current_offset = (offset_x, offset_y)

        # Soft drop shadow so the page stands out from the canvas
        for spread, shade in ((6, "#0b0c0f"), (3, "#08090b")):
            self.canvas.create_rectangle(
                offset_x - spread + 3, offset_y - spread + 5,
                offset_x + scaled_width + spread + 3, offset_y + scaled_height + spread + 5,
                fill=shade, outline="",
            )
        self.canvas.create_image(
            offset_x, offset_y, anchor=tk.NW, image=self.current_photo
        )

        question = self.data[self.current_index]
        parts = question.get("questionParts", [])
        family = self.font_bold.actual()["family"]
        for idx, part in enumerate(parts):
            coords = part.get("coordinates", [])
            if len(coords) != 4:
                continue
            colour = PART_COLOURS[idx % len(PART_COLOURS)]
            x1, y1, x2, y2 = coords
            sx1 = offset_x + x1 * scale
            sy1 = offset_y + y1 * scale
            sx2 = offset_x + x2 * scale
            sy2 = offset_y + y2 * scale
            self.canvas.create_rectangle(sx1, sy1, sx2, sy2, outline=colour, width=2)
            label = part.get("text", "")
            if label:
                # Badge text scales with the box, so labels don't swamp a zoomed-out page
                label_size = max(7, min(14, int((sy2 - sy1) * 0.55)))
                label_padding = max(1, label_size // 4)
                label_font = (family, label_size, "bold")
                # Label badge sits just above the box's top-left corner
                text_id = self.canvas.create_text(
                    sx1 + label_padding,
                    sy1 - label_padding,
                    anchor=tk.SW,
                    fill="#111318",
                    font=label_font,
                    text=label,
                )
                bx1, by1, bx2, by2 = self.canvas.bbox(text_id)
                badge = self.canvas.create_rectangle(
                    bx1 - label_padding, by1 - label_padding // 2,
                    bx2 + label_padding, by2 + label_padding // 2,
                    fill=colour, outline="",
                )
                self.canvas.tag_lower(badge, text_id)


if __name__ == "__main__":
    viewer = PartsViewer()
    viewer.mainloop()
