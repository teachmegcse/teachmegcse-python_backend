import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from PIL import Image, ImageTk


class PartsViewer(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Question Parts Viewer")
        self.geometry("1200x900")

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

        self._build_ui()
        self._bind_keys()

    def _build_ui(self) -> None:
        controls = ttk.Frame(self, padding=8)
        controls.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(controls, text="JSON path:").pack(side=tk.LEFT)
        self.json_entry = ttk.Entry(controls, width=60)
        self.json_entry.pack(side=tk.LEFT, padx=6)
        ttk.Button(controls, text="Browse", command=self._browse_json).pack(
            side=tk.LEFT
        )

        ttk.Label(controls, text="Images folder:").pack(side=tk.LEFT, padx=(12, 0))
        self.images_entry = ttk.Entry(controls, width=40)
        self.images_entry.pack(side=tk.LEFT, padx=6)
        ttk.Button(controls, text="Browse", command=self._browse_images).pack(
            side=tk.LEFT
        )

        ttk.Button(controls, text="Load", command=self._load_data).pack(
            side=tk.LEFT, padx=12
        )

        content = ttk.Frame(self, padding=8)
        content.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        left = ttk.Frame(content)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(left, bg="#1f1f1f", highlightthickness=0)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self._on_canvas_resize)
        self.canvas.bind("<ButtonPress-1>", self._start_pan)
        self.canvas.bind("<B1-Motion>", self._pan)

        nav = ttk.Frame(left, padding=(0, 8, 0, 0))
        nav.pack(side=tk.BOTTOM, fill=tk.X)
        ttk.Button(nav, text="Prev", command=self._prev_question).pack(side=tk.LEFT)
        ttk.Button(nav, text="Next", command=self._next_question).pack(
            side=tk.LEFT, padx=6
        )
        ttk.Button(nav, text="Zoom -", command=self._zoom_out).pack(
            side=tk.LEFT, padx=6
        )
        ttk.Button(nav, text="Zoom +", command=self._zoom_in).pack(side=tk.LEFT)
        ttk.Button(nav, text="Reset Zoom", command=self._reset_zoom).pack(
            side=tk.LEFT, padx=6
        )
        self.status_label = ttk.Label(nav, text="No data loaded")
        self.status_label.pack(side=tk.RIGHT)

        right = ttk.Frame(content, width=360)
        right.pack(side=tk.RIGHT, fill=tk.Y)

        ttk.Label(right, text="Questions").pack(anchor=tk.W)
        self.listbox = tk.Listbox(right, height=12)
        self.listbox.pack(fill=tk.X, pady=(0, 8))
        self.listbox.bind("<<ListboxSelect>>", self._on_listbox_select)

        ttk.Label(right, text="Question text").pack(anchor=tk.W)
        self.question_text = tk.Text(right, height=14, wrap=tk.WORD)
        self.question_text.pack(fill=tk.BOTH, expand=False, pady=(0, 8))
        self.question_text.configure(state=tk.DISABLED)

        ttk.Label(right, text="Parts").pack(anchor=tk.W)
        self.parts_text = tk.Text(right, height=16, wrap=tk.WORD)
        self.parts_text.pack(fill=tk.BOTH, expand=True)
        self.parts_text.configure(state=tk.DISABLED)

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
            self.listbox.insert(tk.END, f"{number}: {name}")

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
        question = self.data[index]

        self._update_question_text(question)
        self._load_image(question)
        self._reset_zoom()
        self._render_image()

        name = question.get("questionName", "(no name)")
        self.status_label.configure(text=f"{index + 1}/{len(self.data)} - {name}")

    def _update_question_text(self, question: dict) -> None:
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
                self.parts_text.insert(tk.END, f"{idx}. {label}  {coords}\n")
        else:
            self.parts_text.insert(tk.END, "No parts found.")
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
        if self.current_image is None:
            self.canvas.create_text(
                20,
                20,
                anchor=tk.NW,
                fill="#ffffff",
                text="No image loaded",
            )
            return

        canvas_width = max(self.canvas.winfo_width(), 1)
        canvas_height = max(self.canvas.winfo_height(), 1)
        image_width, image_height = self.current_image.size

        scale = (
            min(
                canvas_width / image_width,
                canvas_height / image_height,
            )
            * self.zoom_factor
        )
        scaled_width = int(image_width * scale)
        scaled_height = int(image_height * scale)
        offset_x = (canvas_width - scaled_width) // 2
        offset_y = (canvas_height - scaled_height) // 2
        if offset_x < 0:
            offset_x = 0
        if offset_y < 0:
            offset_y = 0
        pan_x, pan_y = self.pan_offset
        offset_x += pan_x
        offset_y += pan_y

        resized = self.current_image.resize((scaled_width, scaled_height))
        self.current_photo = ImageTk.PhotoImage(resized)

        self.current_scale = scale
        self.current_offset = (offset_x, offset_y)

        self.canvas.create_image(
            offset_x, offset_y, anchor=tk.NW, image=self.current_photo
        )

        question = self.data[self.current_index]
        parts = question.get("questionParts", [])
        label_size = max(8, int(12 * self.zoom_factor))
        label_padding = max(2, int(4 * self.zoom_factor))
        for part in parts:
            coords = part.get("coordinates", [])
            if len(coords) != 4:
                continue
            x1, y1, x2, y2 = coords
            sx1 = offset_x + x1 * scale
            sy1 = offset_y + y1 * scale
            sx2 = offset_x + x2 * scale
            sy2 = offset_y + y2 * scale
            self.canvas.create_rectangle(sx1, sy1, sx2, sy2, outline="#00ff66", width=2)
            label = part.get("text", "")
            if label:
                self.canvas.create_text(
                    sx1 + label_padding,
                    sy1 + label_padding,
                    anchor=tk.NW,
                    fill="#ffd200",
                    font=("TkDefaultFont", label_size),
                    text=label,
                )


if __name__ == "__main__":
    viewer = PartsViewer()
    viewer.mainloop()
