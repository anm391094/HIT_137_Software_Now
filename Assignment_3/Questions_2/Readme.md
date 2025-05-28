# 🦊 Fox's Adventure

**S125 HIT137 SOFTWARE NOW**
**Group Assignment 3 – Question 2**
**Group: CAS/DAN 10**

---

## 📌 Overview

_Fox’s Adventure_ is a 2D side-scrolling platformer game developed using **Python** and **Pygame**. It follows the journey of a courageous fox navigating a forest filled with threats and rewards. Players must dodge enemy hunters, collect magical berries and feathers, and survive through increasing levels of difficulty. The game integrates character movement, attacks, collectibles, and a scoring system — creating a complete and interactive gameplay experience.

This project was created as part of our software development coursework to demonstrate object-oriented programming, basic game logic, and real-time event handling in Python.

---

## 🎮 Gameplay Summary

- You play as a **fox** who can **run**, **jump**, and **fire magical fox projectiles**.
- Enemies (hunters) spawn from the right and move toward the player.
- You gain points by defeating enemies and collecting items.
- The game includes a **health bar**, **lives counter**, and a **level-up system** that scales the difficulty.
- If your health drops to zero, you lose a life. Lose all lives and it’s game over — but you can restart.

---

## 🧠 Core Concepts and Features

### 🔸 Object-Oriented Programming

- The game is structured around classes like `Player`, `Projectile`, `Enemy`, and `Collectible`.
- Each object encapsulates its own behavior and interacts with others using sprite groups.

### 🔸 Sprites & Animation

- All characters and items are loaded as image sprites using `pygame.image.load()` and scaled to fit gameplay.
- Sprite groups (`Group()`) are used for collision detection and rendering.

### 🔸 Thematic Projectiles

- The fox doesn't shoot generic bullets — it fires **custom fox-themed projectiles** that reflect its energy or spirit.
- This enhances immersion by tying the attack mechanic directly to the character’s identity.

### 🔸 Health, Lives & Scoring

- A visual **health bar** and **heart icons** track the player’s health and lives.
- Score is displayed on-screen, and defeating enemies or collecting items increases it.

### 🔸 Pause & Game Over Handling

- Pressing `ESC` pauses the game with an overlay.
- If you lose all lives, the game ends with a **Game Over** screen and a prompt to restart by pressing `R`.

---

## 🗂️ File & Folder Structure

```
project/
│
├── fox_adventure.py       # Game code
└── icons/                 # Assets folder
    ├── fox.png            # Player sprite
    ├── hunter.png         # Enemy sprite
    ├── berry.png          # Health item
    ├── feather.png        # Life item
    ├── projectile.png     # Fox-themed projectile
    ├── heart.png          # Heart icon for lives
    └── background.jpg     # Game background
```

> All assets must be in the `icons/` folder. If the game fails to load, check the paths and image sizes.

---

## 🕹️ Controls

| Key         | Action                  |
| ----------- | ----------------------- |
| Left Arrow  | Move left               |
| Right Arrow | Move right              |
| Spacebar    | Jump                    |
| F           | Shoot                   |
| ESC         | Pause/Resume            |
| R           | Restart after Game Over |

---

## 🔄 Game Flow

1. Game starts at **Level 1**.
2. Enemies and collectibles spawn at intervals.
3. Reaching a certain score threshold increases the level:

   - Level 2 at 1000 points
   - Level 3 at 2500 points (stronger enemies)

4. The game ends when all lives are lost, but can be restarted instantly.

---

## 💬 Reflections

This project was both technically challenging and creatively rewarding. We practiced modular design and real-time game logic while paying attention to detail and user experience. Customizing the projectiles as fox-themed elements was a deliberate design choice to keep the visual identity consistent and playful.

As a group, we gained experience in:

- Designing game mechanics from scratch
- Managing user input and game states
- Using sprite-based animations and interactions
- Structuring larger Python projects with clarity

---

Sure! Here's your updated **🚀 Running the Game** section, now including the steps to **create and activate a Python virtual environment**, install Pygame, and run the game — all in a clear and professional format:

---

## 🚀 Running the Game

Follow these steps to set up and run the game in a clean Python environment:

### 1️⃣ Make Sure Python 3 is Installed

Check your Python version:

```bash
python --version
# or
python3 --version
```

If it's not installed, download it from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### 2️⃣ Create a Virtual Environment

In your project folder, run:

```bash
python -m venv env
# or
python3 -m venv env
```

This will create a folder called `env/` containing your isolated Python environment.

---

### 3️⃣ Activate the Virtual Environment

- **On Windows:**

```bash
env\Scripts\activate
```

- **On macOS/Linux:**

```bash
source env/bin/activate
```

You should now see `(env)` in your terminal prompt, indicating the environment is active.

---

### 4️⃣ Install Pygame

With the virtual environment active, install Pygame:

```bash
pip install pygame
```

---

### 5️⃣ Run the Game

With everything set up and your environment activated, run:

```bash
python main.py
```

Enjoy the game!

---

## 🔧 Potential Improvements

This version is a working prototype, but there’s room for future enhancement:

- Add background music and sound effects.
- Introduce new enemy types or boss fights.
- Animate player movement and attacks.
- Create a main menu and difficulty settings.
- Store high scores locally or online.

---

## 👥 Contributors

- **Group: CAS/DAN 10**
  _Assignment 3 – Question 2, HIT137 SOFTWARE NOW_

---

## 📅 Submission Info

- **Subject**: HIT137 SOFTWARE NOW
- **Assignment**: Group Assignment 3
- **Unit**: S125
- **Submission Date**: 30/05/2025

---
