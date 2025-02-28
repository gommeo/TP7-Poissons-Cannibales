import arcade
import os
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
        self.game_view = GameView(self, "./assets/2dfish/body_parts_and_spriter_file/icon.png")
        self.pause_view = PauseView(self)
        self.options_view = OptionsView(self)
        self.high_score_view = HighScore(self)

    def switch_to_main_menu(self):
        self.window.show_view(self.main_menu)

    def switch_to_game_view(self):
        self.window.show_view(self.game_view)

    def switch_to_pause_view(self):
        self.window.show_view(self.pause_view)

    def switch_to_options_view(self):
        self.window.show_view(self.options_view)

    def switch_to_high_score_view(self):
        self.window.show_view(self.high_score_view)

    @staticmethod
    def get_save_file():
        save_file_path = "save_file.txt"

        if os.path.exists(save_file_path):
            file = open(save_file_path, "r")
            content = file.read()
            file.close()

        else:
            pass

    def save_game(self):
        save_file_path = "save_file.txt"

        file = open(save_file_path, "w")
        file.write("")
        file.close()

    def run(self):
        self.get_save_file()
        self.switch_to_main_menu()
        arcade.run()


if __name__ == "__main__":
    manager = Manager()
    manager.run()
