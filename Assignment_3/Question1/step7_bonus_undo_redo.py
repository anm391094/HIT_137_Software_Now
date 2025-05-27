# In __init__()
self.history = []
self.future = []
# In update_resize() or apply_grayscale()
self.history.append(self.original_crop.copy())
self.future.clear()
# In show_cropped_image()
tk.Button(cropped_window, text="Undo", command=self.undo_action).pack(pady=5)
tk.Button(cropped_window, text="Redo", command=self.redo_action).pack(pady=5)
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
