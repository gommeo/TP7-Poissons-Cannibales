import arcade
import math
from PIL import Image
from fish_npc import Fish

img = Image.open("./assets/2dfish/body_parts_and_spriter_file/icon.png")
width, height = img.size

SCREEN_WIDTH = 1164
SCREEN_HEIGHT = 764


class GameView(arcade.View):
    def __init__(self, manager, player_fish_path):
        super().__init__()

        self.manager = manager
        self.player_fish_path = player_fish_path
        self.player = None
        self.player_size = None
        self.sprite_list = None
        self.background = None

        self.up = None
        self.down = None
        self.left = None
        self.right = None

        self.setup()

    def setup(self):
        self.background = arcade.Sprite("./assets/Background.png")
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = SCREEN_HEIGHT / 2

        self.player_size = 2000
        self.player = arcade.Sprite(self.player_fish_path, math.sqrt(self.player_size/(width * height)))
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2

        self.sprite_list = arcade.SpriteList()

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def on_draw(self):
        self.clear()

        self.draw_background()
        arcade.draw_sprite(self.player)
        self.sprite_list.draw()

    def draw_background(self):
        arcade.draw_sprite(self.background)

    def on_update(self, delta_time):
        self.move_player()
        self.check_boundaries()

        for i in self.sprite_list:
            i.on_update()

    def move_player(self):
        if self.up:
            self.player.center_y += 5

        if self.down:
            self.player.center_y -= 5

        if self.left:
            self.player.center_x -= 5

        if self.right:
            self.player.center_x += 5

    def check_boundaries(self):
        pass

    @staticmethod
    def flip_image(image_path):
        image = Image.open(image_path)
        return image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.manager.switch_to_pause_view()

        if key == arcade.key.W or key == arcade.key.UP:
            self.up = True

        if key == arcade.key.S or key == arcade.key.DOWN:
            self.down = True

        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left = True

        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.right = True

        if key == arcade.key.SPACE:
            self.sprite_list.append(Fish(self.player_size))

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up = False

        if key == arcade.key.S or key == arcade.key.DOWN:
            self.down = False

        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left = False

        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.right = False
