# 📸 HIT137 Assignment 3 – Question 1: Desktop Image Editor

This project is a Python desktop application developed using **Tkinter** and **OpenCV** for image editing. It demonstrates key Object-Oriented Programming (OOP) concepts, GUI design, and real-time image processing.

---

## 🎯 Project Objectives

- Apply Python OOP principles
- Build GUI with Tkinter
- Use OpenCV for image processing
- Develop interactive features like cropping, resizing, and saving
- Implement optional enhancements: grayscale filter, undo/redo, and keyboard shortcuts

---

## ✅ Features Implemented

| Feature                          | Status |
|----------------------------------|--------|
| Load image from device           | ✅     |
| Display image on GUI             | ✅     |
| Draw cropping rectangle          | ✅     |
| Crop and show new image          | ✅     |
| Resize with slider               | ✅     |
| Save cropped image               | ✅     |
| Grayscale filter (bonus)         | ✅     |
| Keyboard shortcut Ctrl+S (bonus) | ✅     |
| Undo and Redo functionality      | ✅     |

---

## 🧠 How It Works – Step-by-Step Files

Each task was built as a separate Python file for clarity:

| File                       | Description                             |
|----------------------------|-----------------------------------------|
| `step1_load_image.py`      | Load and display an image               |
| `step2_crop_image.py`      | Crop using mouse interaction            |
| `step3_resize_slider.py`   | Add slider to resize cropped image      |
| `step4_save_image.py`      | Save resized image to local file        |
| `step5_bonus_grayscale.py`| Apply grayscale filter (extra feature)  |
| `step6_bonus_keyboard_shortcut.py` | Ctrl+S shortcut to save       |
| `step7_bonus_undo_redo.py` | Implement undo and redo                 |
| `app.py`                   | Final version with all features         |

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🖼️ OpenCV (`opencv-python`)
- 🪟 Tkinter (Python standard GUI)
- 🧱 PIL (`Pillow` – for image conversion)

---

## ▶️ How to Run

### 📦 1. Install dependencies

```bash
pip install opencv-python pillow

python3 app.py


