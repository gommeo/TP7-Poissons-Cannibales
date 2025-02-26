import arcade
from PIL import Image

SCREEN_WIDTH = 1164
SCREEN_HEIGHT = 764


class GameView(arcade.View):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.background = None

        self.setup()

    def setup(self):
        self.background = arcade.Sprite("./assets/Background.png")
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear()

        self.draw_background()

    def draw_background(self):
        arcade.draw_sprite(self.background)

    def on_update(self, delta_time):
        pass

    @staticmethod
    def flip_image(image_path):
        image = Image.open(image_path)
        return image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.manager.switch_to_pause_view()
