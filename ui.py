import tkinter as tk
from tkinter import messagebox, simpledialog
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label, Frame, Combobox
from game_logic import GameLogic
from leaderboard import show_leaderboard, save_score
from timer import GameTimer
from utils import get_hint, calculate_score, play_sound
from PIL import Image, ImageTk
import os

class NumberGuessingUI:
    def __init__(self, root):
        self.root = root
        self.style = Style("superhero")
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Load background
        bg_path = "assets/bg.jpg"
        if os.path.exists(bg_path):
            self.bg_image = Image.open(bg_path).resize((500, 400))
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = Frame(self.root, padding=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.sound_on = True  # sound toggle

        # Load icons
        def load_icon(name, size=(25, 25)):
            path = f"assets/{name}"
            return ImageTk.PhotoImage(Image.open(path).resize(size)) if os.path.exists(path) else None

        self.trophy_icon = load_icon("trophy.png")
        self.question_icon = load_icon("question_mark.png")
        self.sound_on_icon = load_icon("sound_on.png")
        self.sound_off_icon = load_icon("sound_off.png")

        # Difficulty
        self.difficulty = tk.StringVar()
        Label(self.frame, text="Choose Difficulty:", font=("Arial", 14)).pack(pady=10)
        self.level_menu = Combobox(self.frame, textvariable=self.difficulty,
                                   values=["Easy", "Medium", "Hard", "Impossible"], font=("Arial", 12))
        self.level_menu.pack()
        self.level_menu.current(0)

        Button(self.frame, text="Start Game", bootstyle="success", command=self.start_game).pack(pady=10)

        # Inputs and Outputs
        self.guess_input = Entry(self.frame, font=("Arial", 12))
        self.guess_button = Button(self.frame, text="Guess", command=self.check_guess)
        self.feedback_label = Label(self.frame, font=("Arial", 12))
        self.hint_label = Label(self.frame, font=("Arial", 10))
        self.timer_label = Label(self.frame, font=("Arial", 10))

        # Buttons with Icons
        Button(self.frame, image=self.trophy_icon, text=" Leaderboard", compound="left",
               bootstyle="info", command=show_leaderboard).pack(pady=5)

        self.sound_btn = Button(self.frame, image=self.sound_on_icon, command=self.toggle_sound)
        self.sound_btn.pack(pady=5)

        Button(self.frame, text="🔁 Restart", bootstyle="warning", command=self.reset_ui).pack(side="left", padx=10, pady=10)
        Button(self.frame, text="❌ Exit", bootstyle="danger", command=self.root.quit).pack(side="right", padx=10, pady=10)

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        new_icon = self.sound_on_icon if self.sound_on else self.sound_off_icon
        self.sound_btn.configure(image=new_icon)

    def start_game(self):
        self.logic = GameLogic(self.difficulty.get())
        self.timer = GameTimer(self.timer_label)
        self.timer.start()

        self.guess_input.pack(pady=10)
        self.guess_button.pack(pady=5)
        self.feedback_label.pack(pady=5)
        self.hint_label.pack()
        self.timer_label.pack(pady=5)

        self.guess_input.focus()
        self.guess_input.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.hint_label.config(text="")

    def check_guess(self):
        try:
            guess = int(self.guess_input.get())
            result = self.logic.check_guess(guess)

            if result == "correct":
                self.timer.stop()
                if self.sound_on:
                    play_sound("correct")
                self.feedback_label.config(text="✅ Correct!", foreground="green")
                score = calculate_score(self.logic.attempts, self.timer.elapsed, self.difficulty.get())
                name = simpledialog.askstring("You Win!", "Enter your name for leaderboard:")
                if name:
                    save_score(name, score, self.difficulty.get(), self.timer.elapsed, self.logic.attempts)
                self.reset_ui()

            elif result == "low":
                self.feedback_label.config(text="📉 Too Low!", foreground="orange")
                self.hint_label.config(text=get_hint(guess, self.logic.number))
                if self.sound_on:
                    play_sound("wrong")
            else:
                self.feedback_label.config(text="📈 Too High!", foreground="orange")
                self.hint_label.config(text=get_hint(guess, self.logic.number))
                if self.sound_on:
                    play_sound("wrong")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number")

    def reset_ui(self):
        self.guess_input.pack_forget()
        self.guess_button.pack_forget()
        self.feedback_label.pack_forget()
        self.hint_label.pack_forget()
        self.timer_label.pack_forget()
        if hasattr(self, 'timer'):
            self.timer.stop()
