import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Step 1: Load Image")

        self.image = None
        self.tk_image = None

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='gray')
        self.canvas.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)

    def display_image(self, img):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        self.tk_image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)
        self.canvas.image = self.tk_image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
