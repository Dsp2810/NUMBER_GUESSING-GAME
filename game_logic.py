import random

class GameLogic:
    def __init__(self, level='Easy'):
        self.level = level
        self.number = self._generate_number()
        self.attempts = 0
        self.max_attempts = 10  # Optional limit

    def _generate_number(self):
        ranges = {'Easy': 10, 'Medium': 50, 'Hard': 100, 'Impossible': 1000}
        return random.randint(1, ranges.get(self.level, 10))

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.number:
            return "correct"
        elif guess < self.number:
            return "low"
        else:
            return "high"
