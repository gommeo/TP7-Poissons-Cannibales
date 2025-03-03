import arcade
from math import sqrt, floor, ceil
from random import randint, choice
from PIL import Image

image = Image.open("./assets/2dfish/body_parts_and_spriter_file/icon.png")
width = 498
height = 327

fish_textures = {
    "black_idle" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_black_idle.png").get_texture_grid(size=(498, 327), columns=4, count=20),
    "black_swim" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_black_swim.png").get_texture_grid(size=(498, 327), columns=4, count=12),
    "blue_idle" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_blue_idle.png").get_texture_grid(size=(498, 327), columns=4, count=20),
    "blue_swim" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_blue_swim.png").get_texture_grid(size=(498, 327), columns=4, count=12),
    "green_idle" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_green_idle.png").get_texture_grid(size=(498, 327), columns=4, count=20),
    "green_swim" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_green_swim.png").get_texture_grid(size=(498, 327), columns=4, count=12),
    "purple_idle" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_purple_idle.png").get_texture_grid(size=(498, 327), columns=4, count=20),
    "purple_swim" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_purple_swim.png").get_texture_grid(size=(498, 327), columns=4, count=12),
    "red_idle" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_red_idle.png").get_texture_grid(size=(498, 327), columns=4, count=20),
    "red_swim" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_red_swim.png").get_texture_grid(size=(498, 327), columns=4, count=12),
    "yellow_idle" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_yellow_idle.png").get_texture_grid(size=(498, 327), columns=4, count=20),
    "yellow_swim" : arcade.SpriteSheet("./assets/2dfish/spritesheets/__cartoon_fish_06_yellow_swim.png").get_texture_grid(size=(498, 327), columns=4, count=12)
}


class Fish(arcade.Sprite):
    def __init__(self, player_size):
        super().__init__()
        self.player_size = player_size
        self.animation_speed = None
        self.scale_fish = None

        self.change_x = None
        self.center_x = None
        self.center_y = None

        self.colour = None
        self.textures_idle = None
        self.textures_swim = None
        self.current_texture = None
        self.textures = None

        self.animation_update_time = None
        self.time_since_last_swap = None

        self.setup()

    def setup(self):
        self.animation_speed = 5
        self.scale_fish = randint(round(0.2 * self.player_size), round(3 * self.player_size))
        self.scale = sqrt(self.scale_fish / (width * height))

        self.change_x = choice([(3000 / self.scale_fish) + 3, (-3000 / self.scale_fish) - 3])
        if self.change_x > 0:
            if self.change_x > 10:
                self.change_x = 10
            self.center_x = -sqrt((self.scale_fish * width) / height) / 2
        if self.change_x < 0:
            if self.change_x < -10:
                self.change_x = -10
            self.center_x = 1164 + sqrt((self.scale_fish * width) / height) / 2

        self.center_y = randint(ceil(sqrt((self.scale_fish * height) / width) / 2),
                                764 - floor(sqrt((self.scale_fish * height) / width) / 2))

        self.colour = choice(["black", "green", "purple", "red", "yellow"])

        if self.change_x > 0:
            self.textures_idle = [texture.flip_left_right() for texture in fish_textures[self.colour + "_idle"]]
            self.textures_swim = [texture.flip_left_right() for texture in fish_textures[self.colour + "_idle"]]
        else:
            self.textures_idle = fish_textures[self.colour + "_idle"]
            self.textures_swim = fish_textures[self.colour + "_swim"]
        self.current_texture = 0
        self.textures = self.textures_swim
        self.set_texture(self.current_texture)

        self.animation_update_time = 1.0 / self.animation_speed
        self.time_since_last_swap = 0.0

    def on_update(self, delta_time: float = 1 / 60):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                if self.textures == self.textures_swim:
                    self.textures = self.textures_idle
                else:
                    self.textures = self.textures_swim

                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0

        if self.textures == self.textures_swim:
            self.center_x += self.change_x

        if self.center_x < -sqrt((self.scale_fish * width)/height) or self.center_x > 1164 + sqrt((self.scale_fish * width)/height):
            self.destroy_fish()

    def destroy_fish(self):
        self.remove_from_sprite_lists()
        del self
