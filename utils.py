# utils.py
import random
from playsound import playsound

def get_hint(guess, actual):
    diff = abs(guess - actual)
    if diff == 0:
        return "🔥 Spot on!"
    elif diff <= 3:
        return "🌶 Very hot!"
    elif diff <= 7:
        return "🔥 Hot!"
    elif diff <= 15:
        return "🌤 Warm"
    else:
        return "❄️ Cold"

def calculate_score(attempts, time_taken, level):
    base_score = max(100 - (attempts * 5 + time_taken), 10)
    difficulty_multiplier = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3,
        "Impossible": 5
    }
    return base_score * difficulty_multiplier.get(level, 1)

def play_sound(result):
    if result == "correct":
        playsound("assets/sounds/correct.mp3", block=False)
    else:
        playsound("assets/sounds/wrong.mp3", block=False)
def reset_ui(ui):
    ui.guess_input.pack_forget()
    ui.guess_button.pack_forget()
    ui.feedback_label.config(text="")
    ui.hint_label.config(text="")
    ui.timer_label.config(text="⏱ Time: 0s")
    ui.logic = None
    ui.timer.stop()
    ui.difficulty.set("Easy")
    ui.level_menu.current(0)
    ui.root.update_idletasks()  # Refresh the UI
    ui.root.focus_set()  # Reset focus to the main window
    ui.guess_input.delete(0, 'end')
    ui.guess_input.focus()  # Focus back on the input field
    ui.feedback_label.pack_forget()
    ui.hint_label.pack_forget()
    ui.timer_label.pack_forget()
    ui.timer_label.pack(pady=5)
    ui.guess_input.pack(pady=10)
    ui.guess_button.pack(pady=5)
    ui.feedback_label.pack(pady=5)
    ui.hint_label.pack()
    ui.timer.start()  # Restart the timer
    ui.root.update()  # Ensure the UI updates immediately

def save_score(name, score, level, time_taken, attempts):
    scores = load_scores()
    scores.append({
        "name": name,
        "score": score,
        "level": level,
        "time": time_taken,
        "attempts": attempts
    })
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]  # Top 10 only
    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=2)
def load_scores():
    try:
        with open("scores.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
import json
import tkinter as tk

from ttkbootstrap import Toplevel, Label
def show_leaderboard():
    scores = load_scores()
    top = Toplevel()
    top.title("🏆 Leaderboard")
    Label(top, text="Top Players", font=("Arial", 16, "bold")).pack(pady=10)

    for entry in scores:
        text = f"{entry['name']} - {entry['score']} pts | Level: {entry['level']} | Time: {entry['time']}s | Attempts: {entry['attempts']}"
        Label(top, text=text, font=("Arial", 12)).pack()
def get_random_number(level):
    ranges = {'Easy': 10, 'Medium': 50, 'Hard': 100, 'Impossible': 1000}
    return random.randint(1, ranges.get(level, 10))
def check_guess(guess, number):
    if guess == number:
        return "correct"
    elif guess < number:
        return "low"
    else:
        return "high"
def generate_number(level):
    ranges = {'Easy': 10, 'Medium': 50, 'Hard': 100, 'Impossible': 1000}
    return random.randint(1, ranges.get(level, 10))
