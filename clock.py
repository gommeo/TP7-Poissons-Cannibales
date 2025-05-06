from arcade.clock import Clock


class GameClock(Clock):
    def __init__(self):
        super().__init__()
        self.running = False
        self.elapsed_time = 0.0

    def reset(self):
        self.elapsed_time = 0.0
        self.running = True

    def turn_on(self):
        self.running = True

    def turn_off(self):
        self.running = False

    def get_time(self):
        return self.elapsed_time

    def on_update(self, delta_time: float):
        if self.running:
            self.elapsed_time += delta_time
