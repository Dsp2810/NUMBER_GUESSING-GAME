# leaderboard.py
import json
import tkinter as tk
from ttkbootstrap import Toplevel, Label

LEADERBOARD_FILE = "scores.json"

def load_scores():
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

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
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(scores, file, indent=2)

def show_leaderboard():
    scores = load_scores()
    top = Toplevel()
    top.title("🏆 Leaderboard")
    Label(top, text="Top Players", font=("Arial", 16, "bold")).pack(pady=10)

    for entry in scores:
        text = f"{entry['name']} - {entry['score']} pts | Level: {entry['level']} | Time: {entry['time']} | Attempts: {entry['attempts']}"
        Label(top, text=text, font=("Arial", 12)).pack()