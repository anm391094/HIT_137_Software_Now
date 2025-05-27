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
        cropped = self.image[y1:y2, x1:x2]
        self.show_cropped_image(cropped)

def show_cropped_image(self, cropped_img):
    cropped_window = tk.Toplevel(self.root)
    cropped_window.title("Cropped Image")

    rgb_crop = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
    pil_crop = Image.fromarray(rgb_crop)
    tk_crop = ImageTk.PhotoImage(pil_crop)

    label = tk.Label(cropped_window, image=tk_crop)
    label.image = tk_crop
    label.pack()
