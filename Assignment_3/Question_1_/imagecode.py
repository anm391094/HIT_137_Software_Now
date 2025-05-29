import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import numpy as np

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor - HIT137 Assignment 3")

        # Canvas placeholders
        self.original_canvas = tk.Canvas(root, width=400, height=400)
        self.cropped_canvas = tk.Canvas(root, width=400, height=400)
        self.original_canvas.grid(row=0, column=0)
        self.cropped_canvas.grid(row=0, column=1)


        load_btn = tk.Button(root, text="Load Image", command=self.load_image)
        load_btn.grid(row=1, column=0, pady=5)

        save_btn = tk.Button(root, text="Save Cropped Image", command=self.save_image)
        save_btn.grid(row=1, column=1, pady=5)


        self.slider = tk.Scale(root, from_=10, to=200, orient='horizontal', label='Resize %', command=self.resize_image)
        self.slider.set(100)
        self.slider.grid(row=2, column=1)


        self.image = None
        self.tk_image = None
        self.start_x = self.start_y = 0
        self.rect = None
        self.crop_rect = None
        self.cropped_img = None

        self.original_canvas.bind("<Button-1>", self.start_crop)
        self.original_canvas.bind("<B1-Motion>", self.draw_crop)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        self.image = cv2.imread(file_path)
        self.display_image(self.image, self.original_canvas)

    def display_image(self, img, canvas):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil = img_pil.resize((400, 400))
        self.tk_image = ImageTk.PhotoImage(img_pil)
        canvas.create_image(0, 0, anchor='nw', image=self.tk_image)

    def start_crop(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.original_canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def draw_crop(self, event):
        self.original_canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
        x1, y1, x2, y2 = self.start_x, self.start_y, event.x, event.y
        h, w = self.image.shape[:2]
        x_scale = w / 400
        y_scale = h / 400
        x1_img, x2_img = int(min(x1, x2) * x_scale), int(max(x1, x2) * x_scale)
        y1_img, y2_img = int(min(y1, y2) * y_scale), int(max(y1, y2) * y_scale)
        self.crop_rect = self.image[y1_img:y2_img, x1_img:x2_img]
        self.cropped_img = self.crop_rect.copy()
        self.display_image(self.crop_rect, self.cropped_canvas)

    def resize_image(self, value):
        if self.crop_rect is not None:
            percent = int(value) / 100.0
            width = int(self.crop_rect.shape[1] * percent)
            height = int(self.crop_rect.shape[0] * percent)
            resized = cv2.resize(self.crop_rect, (width, height))
            self.cropped_img = resized
            self.display_image(resized, self.cropped_canvas)

    def save_image(self):
        if self.cropped_img is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.cropped_img)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("850x450")
    app = ImageEditor(root)
    root.mainloop()

