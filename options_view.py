import arcade


class OptionsView(arcade.View):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
