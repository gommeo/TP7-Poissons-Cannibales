import arcade
from main_menu import MainMenu
from game_view import GameView
from pause_view import PauseView
from options_view import OptionsView
from high_score import HighScore

SCREEN_WIDTH = 1164
SCREEN_HEIGHT = 764


class Manager:
    def __init__(self):
        self.window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "POISSONS CANNIBALES")
        self.main_menu = MainMenu(self)
        self.game_view = GameView(self)
        self.pause_view = PauseView(self)
        self.options_view = OptionsView(self)
        self.high_score = HighScore(self)

    def switch_to_main_menu(self):
        self.window.show_view(self.main_menu)

    def switch_to_game_view(self):
        self.window.show_view(self.game_view)

    def switch_to_pause_view(self):
        self.window.show_view(self.pause_view)

    def switch_to_options_view(self):
        self.window.show_view(self.options_view)

    def switch_to_high_score(self):
        self.window.show_view(self.high_score)

    def run(self):
        self.switch_to_main_menu()
        arcade.run()


if __name__ == "__main__":
    manager = Manager()
    manager.run()
