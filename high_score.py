import arcade


class HighScore(arcade.View):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
