# In show_cropped_image()
tk.Button(cropped_window, text="Save Image", command=self.save_image).pack(pady=5)
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
