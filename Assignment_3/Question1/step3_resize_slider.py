# Add to show_cropped_image()
self.original_crop = cropped_img

self.slider = tk.Scale(cropped_window, from_=10, to=200, orient='horizontal',
                       label='Resize %', command=self.update_resize)
self.slider.set(100)
self.slider.pack(pady=5)
def update_resize(self, value):
    value = int(value)
    width = int(self.original_crop.shape[1] * value / 100)
    height = int(self.original_crop.shape[0] * value / 100)

    resized = cv2.resize(self.original_crop, (width, height))
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)
    self.tk_crop = ImageTk.PhotoImage(pil_img)

    self.crop_label.configure(image=self.tk_crop)
    self.crop_label.image = self.tk_crop
