import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        self.image = None
        self.tk_image = None
        self.start_x = self.start_y = 0
        self.rect = None

        # For Undo/Redo
        self.history = []
        self.future = []

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='gray')
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)

    def display_image(self, img):
        self.cv_image = img
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        self.tk_image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)
        self.canvas.image = self.tk_image

    def on_mouse_down(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.rect:
            self.canvas.delete(self.rect)

    def on_mouse_drag(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='red')

    def on_mouse_up(self, event):
        end_x, end_y = event.x, event.y
        x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)

        if self.image is not None:
            cropped = self.cv_image[y1:y2, x1:x2]
            self.show_cropped_image(cropped)

    def show_cropped_image(self, cropped_img):
        self.original_crop = cropped_img
        self.resized_crop = cropped_img.copy()
        self.history.clear()
        self.future.clear()

        cropped_window = tk.Toplevel(self.root)
        cropped_window.title("Cropped Image")

        rgb_crop = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
        pil_crop = Image.fromarray(rgb_crop)
        self.tk_crop = ImageTk.PhotoImage(pil_crop)

        self.crop_label = tk.Label(cropped_window, image=self.tk_crop)
        self.crop_label.image = self.tk_crop
        self.crop_label.pack()

        # Slider
        self.slider = tk.Scale(cropped_window, from_=10, to=200, orient='horizontal',
                               label='Resize %', command=self.update_resize)
        self.slider.set(100)
        self.slider.pack(pady=5)

        # Buttons
        tk.Button(cropped_window, text="Save Image", command=self.save_image).pack(pady=5)
        tk.Button(cropped_window, text="Grayscale", command=self.apply_grayscale).pack(pady=5)
        tk.Button(cropped_window, text="Undo", command=self.undo_action).pack(pady=5)
        tk.Button(cropped_window, text="Redo", command=self.redo_action).pack(pady=5)

        # Keyboard shortcut for save
        cropped_window.bind('<Control-s>', lambda event: self.save_image())

    def update_resize(self, value):
        if self.original_crop is not None:
            self.history.append(self.original_crop.copy())
            self.future.clear()

        value = int(value)
        width = int(self.original_crop.shape[1] * value / 100)
        height = int(self.original_crop.shape[0] * value / 100)

        resized = cv2.resize(self.original_crop, (width, height))
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)
        self.tk_crop = ImageTk.PhotoImage(pil_img)

        self.crop_label.configure(image=self.tk_crop)
        self.crop_label.image = self.tk_crop

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg *.jpeg"),
                                                            ("All files", "*.*")])
        if file_path:
            resized = cv2.resize(self.original_crop, (
                int(self.original_crop.shape[1] * self.slider.get() / 100),
                int(self.original_crop.shape[0] * self.slider.get() / 100)
            ))
            cv2.imwrite(file_path, resized)

    def apply_grayscale(self):
        if self.original_crop is not None:
            self.history.append(self.original_crop.copy())
            self.future.clear()
            gray = cv2.cvtColor(self.original_crop, cv2.COLOR_BGR2GRAY)
            gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            self.original_crop = gray_bgr
            self.update_resize(self.slider.get())

    def undo_action(self):
        if self.history:
            self.future.append(self.original_crop.copy())
            self.original_crop = self.history.pop()
            self.update_resize(self.slider.get())

    def redo_action(self):
        if self.future:
            self.history.append(self.original_crop.copy())
            self.original_crop = self.future.pop()
            self.update_resize(self.slider.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
