# timer.py
import time
import threading

class GameTimer:
    def __init__(self, label):
        self.label = label
        self.elapsed = 0
        self.running = False
        self.thread = None

    def _update(self):
        start_time = time.time()
        while self.running:
            self.elapsed = int(time.time() - start_time)
            self.label.config(text=f"⏱ Time: {self.elapsed}s")
            time.sleep(1)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._update, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.label.config(text=f"⏱ Time: {self.elapsed}s")
