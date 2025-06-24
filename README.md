# 🎯 Number Guessing Game

Welcome to the **Number Guessing Game** – a fun and interactive game built using **Python** and **Tkinter**, enhanced with modern styling, sound effects, timer, hints, and a leaderboard!

---

## 🚀 Features

- 🎨 Beautiful modern GUI using `ttkbootstrap`
- 🔊 Sound effects for right and wrong answers
- 🕒 Real-time timer
- 🧠 Smart hint system to guide your guesses
- 🧩 Difficulty levels: Easy, Medium, Hard, Impossible
- 🏆 Leaderboard tracking top players (local storage)
- 🌗 Dark theme support
- 🔁 Restart and Exit functionality
- 📦 Modular and clean code architecture

---

## 📂 Project Structure

```
number_guessing_game/
├── assets/
│   ├── bg.jpg                # Background image
│   ├── leaderboard.png       # Icon for leaderboard
│   ├── question_mark.png     # Icon for hint or help
│   ├── sound_off.png         # Sound toggle (off)
│   ├── sound_on.png          # Sound toggle (on)
│   └── trophy.png            # Trophy icon
│
├── icons/
│   └── icon.ico              # Window icon file
│
├── sounds/
│   ├── correct.mp3           # Sound for correct guess
│   └── wrong.mp3             # Sound for wrong guess
│
├── game_logic.py             # Game core logic
├── leaderboard.py            # Leaderboard logic and UI
├── main.py                   # Entry point
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── scores.json               # Leaderboard storage
├── timer.py                  # Timer class for tracking duration
├── ui.py                     # User interface (GUI)
└── utils.py                  # Hint logic, scoring, and sound utils
```

---

## 🛠 Installation

1. Clone the repository:
```bash
git clone https://github.com/Dsp2810/NUMBER_GUESSING-GAME.git
cd number-guessing-game
```

2. Install required libraries:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

---

## 📦 Requirements
- `ttkbootstrap`
- `playsound`

You can install them manually:
```bash
pip install ttkbootstrap playsound
```

---

## 🎮 How to Play

1. Launch the game.
2. Select your preferred difficulty.
3. Enter your guesses and use hints to guide you.
4. Try to guess the number in the least attempts and shortest time.
5. See your score and compare with others on the leaderboard.

---

## 🏆 Leaderboard Format
```json
[
  {
    "name": "Dhaval",
    "score": 900,
    "level": "Hard",
    "time": "18",
    "attempts": 2
  }
]
```

---

## 🖼️ Screenshots 

![Game Window](assets/bg.jpg)
```

---

## ✅ To-Do Ideas
- Global leaderboard via Firebase or MySQL
- Animation on correct/wrong guess
- Multiplayer guessing game
- Countdown timer option

---

## 📘 License
MIT License

---

## 👨‍💻 Developer
Made with ❤️ by **Dhaval Patel**
