import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

def setup_style(root):
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('TFrame', background='#1f1f1f')
    style.configure('TButton', background='#333', foreground='white', font=('Segoe UI', 10), padding=6)
    style.map('TButton', background=[('active', '#555')])
    style.configure('TLabel', background='#1f1f1f', foreground='white', font=('Segoe UI', 10))
    style.configure('TScale', troughcolor='#444', background="#ccc")
    style.configure('Horizontal.TScale', sliderlength=18)

class ImageEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('HIT137 Image Editor')
        self.geometry('1000x700')
        self.configure(bg='#1f1f1f')
        setup_style(self)

        self.original = None
        self.current = None
        self.photo = None
        self.display = None
        self.start = None
        self.rect_id = None
        self.history = []
        self.history_idx = -1
        self.max_hist = 20

        self._build_ui()
        self._bind_keys()

    def _build_ui(self):
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label='Load    Ctrl+O', command=self.load_image)
        file_menu.add_command(label='Save    Ctrl+S', command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)
        menu.add_cascade(label='File', menu=file_menu)
        self.config(menu=menu)

        main = ttk.Frame(self)
        main.pack(fill=tk.BOTH, expand=True)
        controls = ttk.Frame(main)
        controls.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        canvas_frame = ttk.Frame(main)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(controls, text='Tools').pack(pady=5)
        ttk.Button(controls, text='📂 Load Image', command=self.load_image).pack(fill=tk.X, pady=3)
        ttk.Button(controls, text='💾 Save Image', command=self.save_image).pack(fill=tk.X, pady=3)
        ttk.Button(controls, text='Undo (Ctrl+Z)', command=self.undo).pack(fill=tk.X, pady=2)
        ttk.Button(controls, text='Redo (Ctrl+Y)', command=self.redo).pack(fill=tk.X, pady=2)
        ttk.Button(controls, text='Grayscale (Ctrl+G)', command=self.grayscale).pack(fill=tk.X, pady=2)
        ttk.Button(controls, text='Blur (Ctrl+B)', command=self.blur).pack(fill=tk.X, pady=2)
        ttk.Button(controls, text='Invert (Ctrl+I)', command=self.invert).pack(fill=tk.X, pady=2)
        ttk.Button(controls, text='Sharpen (Ctrl+E)', command=self.sharpen).pack(fill=tk.X, pady=2)

        ttk.Label(controls, text='Resize (%)').pack(pady=(15, 5))
        resize_frame = ttk.Frame(controls)
        resize_frame.pack(fill=tk.X)
        self.zoom_var = tk.IntVar(value=100)
        self.slider = ttk.Scale(resize_frame, from_=10, to=200, orient='horizontal', command=self.on_zoom)
        self.slider.set(100)
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Spinbox(resize_frame, from_=10, to=200, textvariable=self.zoom_var, width=5, command=self.on_spin).pack(side=tk.LEFT, padx=(5, 0))

        self.status = ttk.Label(self, text='Ready', anchor='w')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas = tk.Canvas(canvas_frame, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<ButtonPress-1>', self.on_press)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_release)

    def _bind_keys(self):
        shortcuts = {
            '<Control-o>': self.load_image,
            '<Control-s>': self.save_image,
            '<Control-z>': self.undo,
            '<Control-y>': self.redo,
            '<Control-g>': self.grayscale,
            '<Control-b>': self.blur,
            '<Control-i>': self.invert,
            '<Control-e>': self.sharpen
        }
        for key, func in shortcuts.items():
            self.bind(key, lambda e, f=func: f())

    def record_state(self):
        self.history = self.history[:self.history_idx + 1]
        self.history.append(self.current.copy())
        if len(self.history) > self.max_hist:
            self.history.pop(0)
        else:
            self.history_idx += 1

    def undo(self):
        if self.history_idx > 0:
            self.history_idx -= 1
            self.current = self.history[self.history_idx].copy()
            self.reset_zoom()
            self._draw(self.current)
            self.status.config(text='Undo')

    def redo(self):
        if self.history_idx < len(self.history) - 1:
            self.history_idx += 1
            self.current = self.history[self.history_idx].copy()
            self.reset_zoom()
            self._draw(self.current)
            self.status.config(text='Redo')

    def _apply(self, func, label):
        if self.current is None: return
        self.current = func(self.current)
        self.record_state()
        self.reset_zoom()
        self._draw(self.current)
        self.status.config(text=label)

    def grayscale(self): self._apply(lambda img: cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2RGB), 'Grayscale')
    def blur(self): self._apply(lambda img: cv2.GaussianBlur(img, (7, 7), 0), 'Blurred')
    def invert(self): self._apply(lambda img: cv2.bitwise_not(img), 'Inverted')
    def sharpen(self): self._apply(lambda img: cv2.filter2D(img, -1, np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])), 'Sharpened')

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[('Images', '*.png *.jpg *.jpeg *.bmp')])
        if not path: return
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.original = img.copy()
        self.current = img.copy()
        self.history = []
        self.history_idx = -1
        self.record_state()
        self.fit_image()
        self.status.config(text='Image Loaded')

    def save_image(self):
        if self.current is None: return
        path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg')])
        if not path: return
        scale = self.zoom_var.get() / 100
        h, w = self.current.shape[:2]
        resized = cv2.resize(self.current, (int(w*scale), int(h*scale)))
        cv2.imwrite(path, cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))
        self.status.config(text='Image Saved')

    def fit_image(self):
        self.update_idletasks()
        cw = self.canvas.winfo_width() or self.winfo_width() - 200
        ch = self.canvas.winfo_height() or self.winfo_height() - 100
        h, w = self.current.shape[:2]
        scale = min(cw/w, ch/h, 1)
        zoom_val = int(scale * 100)
        self.zoom_var.set(zoom_val)
        self.slider.set(zoom_val)
        resized = cv2.resize(self.current, (int(w*scale), int(h*scale)))
        self._draw(resized)

    def reset_zoom(self):
        self.zoom_var.set(100)
        self.slider.set(100)

    def _draw(self, img):
        self.canvas.delete('all')
        self.display = img
        pil_img = Image.fromarray(img)
        self.photo = ImageTk.PhotoImage(pil_img)
        self.canvas.create_image(0, 0, anchor='nw', image=self.photo)

    def on_press(self, e):
        self.start = (e.x, e.y)
        if self.rect_id: self.canvas.delete(self.rect_id)

    def on_drag(self, e):
        if not self.start: return
        if self.rect_id: self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(*self.start, e.x, e.y, outline='gold', width=2)

    def on_release(self, e):
        if self.current is None or not self.start: return
        x0, y0 = self.start
        x1, y1 = e.x, e.y
        dh, dw = self.display.shape[:2]
        sh, sw = self.current.shape[:2]
        fx, fy = sw/dw, sh/dh
        x0, x1 = sorted((int(x0*fx), int(x1*fx)))
        y0, y1 = sorted((int(y0*fy), int(y1*fy)))
        self.current = self.current[y0:y1, x0:x1]
        self.record_state()
        self.reset_zoom()
        self._draw(self.current)
        self.status.config(text=f'Cropped {x1-x0}×{y1-y0}')
        self.start = None

    def on_zoom(self, val):
        if self.current is None: return
        v = float(val)
        self.zoom_var.set(int(v))
        h, w = self.current.shape[:2]
        img = cv2.resize(self.current, (int(w*v/100), int(h*v/100)))
        self._draw(img)
        self.status.config(text=f'Resize: {int(v)}%')

    def on_spin(self):
        val = self.zoom_var.get()
        self.slider.set(val)
        self.on_zoom(val)

if __name__ == '__main__':
    ImageEditor().mainloop()
