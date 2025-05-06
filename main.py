"""
Oscar Gomme
Class pour commencer l'application
TP7-Poissons Cannibales
"""


import arcade
import os
import re
from PIL import Image
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
        self.high_score = []
        self.fish = None

        self.main_menu = None
        self.options_view = None
        self.fish = None
        self.game_view = None
        self.pause_view = None
        self.high_score_view = None

        self.anal_fin = None
        self.body = None
        self.dorsal_fin = None
        self.jaw = None
        self.left_eye = None
        self.pectoral_fin = None
        self.right_eye = None
        self.tail = None

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

    def get_save_file(self):
        save_file_path = "save_file.txt"

        if os.path.exists(save_file_path):
            file = open(save_file_path, "r")
            content = file.read()
            file.close()
            split_content = re.split(r"[\n:]", content)

            self.anal_fin = split_content[1]
            self.body = split_content[3]
            self.dorsal_fin = split_content[5]
            self.jaw = split_content[7]
            self.left_eye = split_content[9]
            self.pectoral_fin = split_content[11]
            self.right_eye = split_content[13]
            self.tail = split_content[15]

            high_score = split_content[16:]
            if high_score[0] != "":
                high_score.pop(len(high_score) - 1)
                self.high_score = [int(x) for x in high_score]
            else:
                self.high_score = []

        else:
            self.anal_fin = "black"
            self.body = "black"
            self.dorsal_fin = "black"
            self.jaw = "black"
            self.left_eye = "black"
            self.pectoral_fin = "black"
            self.right_eye = "black"
            self.tail = "black"

    def save_game(self):
        save_file_path = "save_file.txt"

        file = open(save_file_path, "w")

        string = ""
        o = self.options_view
        string += f"anal_fin:{o.anal_fin}\nbody:{o.body}\ndorsal_fin:{o.dorsal_fin}\njaw:{o.jaw}\nleft_eye:{o.left_eye}\npectoral_fin:{o.pectoral_fin}\nright_eye:{o.right_eye}\ntail:{o.tail}\n"

        for score in self.high_score:
            string += f"{score}\n"

        file.write(string)
        file.close()

    def run(self):
        self.get_save_file()
        self.initialize_classes()
        self.switch_to_main_menu()
        arcade.run()

    def initialize_classes(self):
        self.main_menu = MainMenu(self)
        self.options_view = OptionsView(self)
        self.fish = self.build_fish()
        self.game_view = GameView(self, self.fish)
        self.pause_view = PauseView(self)
        self.high_score_view = HighScore(self)

    def update_highscores(self, new_highscore):
        self.high_score.append(new_highscore)
        self.high_score.sort(reverse=True)

        if len(self.high_score) > 10:
            self.high_score.pop(10)

    def build_fish(self):
        o = self.options_view

        image1 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.anal_fin}/anal_fin.png")
        image2 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.body}/body.png")
        image3 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.dorsal_fin}/dorsal_fin.png")
        image4 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.jaw}/jaw.png")
        image5 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.left_eye}/left_eye_open.png")
        image6 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.pectoral_fin}/pectoral_fin.png")
        image7 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.right_eye}/right_eye_open.png")
        image8 = Image.open(f"./assets/2dfish/body_parts_and_spriter_file/{o.tail}/tail.png")

        canvas_width = 1653
        canvas_height = 1020
        canvas = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

        canvas.paste(image3, (582, 0), mask=image3)
        canvas.paste(image8, (1383, 430), mask=image8)
        canvas.paste(image5, (275, 167), mask=image5)
        canvas.paste(image1, (1150, 746), mask=image1)

        canvas.paste(image2, (134, 128), mask=image2)

        canvas.paste(image7, (368, 171), mask=image7)
        canvas.paste(image6, (894, 733), mask=image6)
        canvas.paste(image4, (0, 584), mask=image4)

        return canvas


if __name__ == "__main__":
    manager = Manager()
    manager.run()
