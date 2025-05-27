# Add to show_cropped_image()
self.original_crop = cropped_img

self.slider = tk.Scale(cropped_window, from_=10, to=200, orient='horizontal',
                       label='Resize %', command=self.update_resize)
self.slider.set(100)
self.slider.pack(pady=5)
