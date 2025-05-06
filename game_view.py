import arcade
from math import sqrt
from random import randint
from PIL import Image
from fish_npc import Fish
from clock import GameClock

img = Image.open("./assets/2dfish/body_parts_and_spriter_file/icon.png")
width, height = img.size

SCREEN_WIDTH = 1164
SCREEN_HEIGHT = 700


class GameView(arcade.View):
    def __init__(self, manager, fish):
        super().__init__()

        self.manager = manager
        self.fish = fish
        self.original_player = None
        self.normal_player = None
        self.flipped_player = None
        self.mirrored_player = None
        self.player = None
        self.player_size = None
        self.sprite_list = None
        self.background = None

        self.up = None
        self.down = None
        self.left = None
        self.right = None

        self.last_key_right = None
        self.running = None
        self.show_hitbox = None
        self.last_key = None
        self.score = None
        self.lives = None
        self.clock = GameClock()

        self.setup()

    def setup(self):
        self.background = arcade.Sprite("./assets/Background.png")
        self.background.center_x = SCREEN_WIDTH / 2
        self.background.center_y = (SCREEN_HEIGHT + 64) / 2

        self.player_size = 2000

        self.flipped_player = arcade.Texture(GameView.flip_image(self.fish))
        self.original_player = arcade.Texture(self.fish)
        self.update_size()
        self.player = self.normal_player
        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2

        self.sprite_list = arcade.SpriteList()

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.running = True
        self.last_key_right = True
        self.show_hitbox = False
        self.last_key = None
        self.score = 0
        self.lives = 3
        self.clock.reset()

    def update_size(self):
        self.normal_player = arcade.Sprite(self.original_player, sqrt(self.player_size / (width * height)))
        self.mirrored_player = arcade.Sprite(self.flipped_player, sqrt(self.player_size / (width * height)))

    def on_draw(self):
        self.clear()

        self.draw_background()
        arcade.draw_sprite(self.player)
        self.sprite_list.draw()

        if self.show_hitbox:
            self.sprite_list.draw_hit_boxes()
            self.player.draw_hit_box()

        # r = arcade.rect.XYWH(100, 720, 100, 30)
        # arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)

        affichage = arcade.Text(f"Score: {self.score}", 50, 735, arcade.color.BARBIE_PINK, width=100, align="center", font_size=24)
        affichage.draw()

        affichage = arcade.Text(f"Lives: {self.lives}", 300, 735, arcade.color.BARBIE_PINK, width=100, align="center", font_size=24)
        affichage.draw()
        affichage = arcade.Text(f"Time: {self.clock.get_time()}", 450, 735, arcade.color.BARBIE_PINK, width=100, align="center", font_size=24)
        affichage.draw()

    def draw_background(self):
        arcade.draw_sprite(self.background)

    def on_update(self, delta_time):
        self.move_player()
        self.check_boundaries()
        self.clock.on_update(delta_time)

        total_fish = 0

        for fish in self.sprite_list:
            fish.on_update()
            if arcade.check_for_collision(fish, self.player):
                if fish.scale_fish > self.player_size and not self.show_hitbox:
                    if fish.scale_fish > 1.5 * self.player_size:
                        self.lives -= 1
                        fish.destroy_fish()

                        if not self.lives:
                            self.manager.update_highscores(self.score)
                            self.setup()
                else:
                    self.score += round(0.1 * fish.scale_fish)
                    self.player_size += round(0.1 * fish.scale_fish)
                    fish.destroy_fish()
                    self.update_size()

            total_fish += fish.scale_fish

        self.check_direction()

        if total_fish < 200000 and len(self.sprite_list) < 20 and self.running:
            self.sprite_list.append(Fish(self.player_size, randint(0, 250)))

        self.score += 1

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
        if self.player.center_x < sqrt((self.player_size * width)/height) / 2:
            self.player.center_x = sqrt((self.player_size * width)/height) / 2
        elif self.player.center_x > SCREEN_WIDTH - sqrt((self.player_size * width)/height) / 2:
            self.player.center_x = SCREEN_WIDTH - sqrt((self.player_size * width)/height) / 2

        if self.player.center_y < sqrt((self.player_size * height)/width) / 2:
            self.player.center_y = sqrt((self.player_size * height)/width) / 2
        elif self.player.center_y > SCREEN_HEIGHT - sqrt((self.player_size * height)/width) / 2:
            self.player.center_y = SCREEN_HEIGHT - sqrt((self.player_size * height)/width) / 2

    def check_direction(self):
        x = self.player.center_x
        y = self.player.center_y

        if not self.last_key_right:
            self.player = self.normal_player
        else:
            self.player = self.mirrored_player

        self.player.center_x = x
        self.player.center_y = y

    @staticmethod
    def flip_image(image):
        return image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.manager.switch_to_pause_view()

        if key == arcade.key.W or key == arcade.key.UP:
            self.up = True

        if key == arcade.key.S or key == arcade.key.DOWN:
            self.down = True
            self.last_key = "s"

        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left = True

            self.last_key_right = False

            if self.last_key == "m":
                self.debug()
                self.last_key = None

        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.right = True

            self.last_key_right = True

        if key == arcade.key.I and self.last_key == "s":
            self.last_key = "i"

        if key == arcade.key.G and self.last_key == "i":
            self.last_key = "g"

        if key == arcade.key.M and self.last_key == "g":
            self.last_key = "m"

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.up = False

        if key == arcade.key.S or key == arcade.key.DOWN:
            self.down = False

        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left = False

            if not self.right:
                self.last_key_right = False

            else:
                self.last_key_right = True

        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.right = False

            if not self.left:
                self.last_key_right = True

            else:
                self.last_key_right = False

    def on_show_view(self):
        self.fish = self.manager.build_fish()

        self.original_player = arcade.Texture(self.fish)
        self.flipped_player = arcade.Texture(GameView.flip_image(self.fish))
        self.update_size()
        self.running = True
        self.clock.turn_on()

    def on_hide_view(self):
        self.running = False
        self.clock.turn_off()

    def debug(self):
        self.show_hitbox = not self.show_hitbox
