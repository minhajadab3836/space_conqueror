# 🚀 Space Conqueror

A 2D **arcade-style space shooter** inspired by Space Invaders, built entirely with Python and Pygame.  
The game features spaceship selection, background music, multiple bullets, real-time statistics, dynamic enemy waves, and a persistent high score system for a polished retro experience. 🚀👾


This project features a main menu, spaceship selection, real-time statistics (kills, accuracy, bullets used), background music, sound effects, and a persistent high score system.

---

## 🧠 Features

- 🎮 **Main Menu** with spaceship selection (1–4)
- 🛰️ Smooth player movement with keyboard
- 💥 Multiple bullets support
- 👾 Dynamic enemy spawning over time
- 🧮 Real-time **statistics**:
  - Aliens destroyed
  - Bullets used
  - Accuracy %
  - Total points
- 📝 **High Score** saved between sessions
- 🎶 Background music and sound effects
- 🧰 Organized asset structure

---

## 🗂 Project Structure

```

Space-Invader/  
├── Assets/  
│ ├── Fonts/  
│ ├── Images/  
│ ├── Sounds/  
│ └── Data/  
│ └── high_score.txt  
├── main.py  
└── README.md

````

---

## 🛠 Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [Pygame](https://pypi.org/project/pygame/)

You can install Pygame using pip:

```bash
pip install pygame
````

---

## ▶️ How to Play

1. **Run the game**:
    

```bash
python3 main.py
```

2. **Controls**:
    
    - `←` / `→` → Move left / right
        
    - `SPACE` → Shoot
        
    - `ESC` (in menu) → Quit the game
        
    - `1`–`4` → Choose spaceship on main menu
        
    - `RETURN` → Restart after Game Over
        
3. **Objective**:
    
    - Destroy as many aliens as possible.
        
    - Keep your accuracy high to earn more points.
        
    - Avoid letting enemies cross the bottom line!
        

---

## 🌟 Scoring System

- ✅ **+10 Points** per alien destroyed
    
- ❌ **−5 Points** for each bullet missed
    
- 🏆 High score is stored in `Assets/Data/high_score.txt`
    

---

## 🖼️ Screenshots

![[Screenshot from 2025-10-13 00-32-00.png]]

![[Screenshot from 2025-10-13 00-32-09.png]]

![[Screenshot from 2025-10-13 00-33-46.png]]

---

## 🧰 Planned Features / Ideas

-  Fullscreen mode toggle (F11)
    
-  Mouse controls for movement & shooting
    
-  Web version (via [Pygbag](https://pygame-web.github.io/))
    
-  Mobile-friendly version (optional)
    
-  Better enemy AI patterns
    
-  Pause menu

---

## 🧑‍💻 Author

**Md Minhaj Adab
📧 Email: [minhajadab06@gmail.com](mailto:minhajadab06@gmail.com)  
⭐ If you like this project, give it a star on [GitHub](https://github.com/minhajadab3836)!

---
