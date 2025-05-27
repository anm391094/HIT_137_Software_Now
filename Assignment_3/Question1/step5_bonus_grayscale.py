# In show_cropped_image()
tk.Button(cropped_window, text="Grayscale", command=self.apply_grayscale).pack(pady=5)
def apply_grayscale(self):
    gray = cv2.cvtColor(self.original_crop, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    self.original_crop = gray_bgr
    self.update_resize(self.slider.get())
