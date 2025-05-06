"""
Oscar Gomme
Class pour montrer les highscores
"""


import arcade
from arcade.gui import UIManager, UITextureButton, UIAnchorLayout

TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")


class HighScore(arcade.View):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.ui = None
        self.highscores = None
        self.text = None

        self.setup()

    def setup(self):
        self.ui = UIManager()
        self.highscores = self.manager.high_score
        self.text = []

        anchor = self.ui.add(UIAnchorLayout())

        button_back = anchor.add(
            UITextureButton(
                text="Back",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",
            align_y=-250
        )

        @button_back.event("on_click")
        def on_click(event):
            self.manager.switch_to_main_menu()

    def on_draw(self):
        self.clear()

        self.ui.draw()

        for i in range(len(self.text)):
            if i == 0:
                affichage = arcade.Text(self.text[i], 1164/2 - 50, 500 - 35*i, font_size=32,
                                        color=arcade.color.GOLD, multiline=False)
            elif i == 1:
                affichage = arcade.Text(self.text[i], 1164/2 - 50, 500 - 35*i, font_size=32,
                                        color=arcade.color.ROMAN_SILVER, multiline=False)
            elif i == 2:
                affichage = arcade.Text(self.text[i], 1164/2 - 50, 500 - 35*i, font_size=32,
                                        color=arcade.color.BRONZE, multiline=False)
            else:
                affichage = arcade.Text(self.text[i], 1164 / 2 - 50, 500 - 35 * i, font_size=32,
                                        color=arcade.color.WILD_BLUE_YONDER, multiline=False)
            affichage.draw()

    def on_show_view(self) -> None:
        self.ui.enable()
        self.highscores = self.manager.high_score
        self.text = []

        for i in range(len(self.highscores)):
            self.text.append(f"{i+1}: {self.highscores[i]}")

    def on_hide_view(self) -> None:
        self.ui.disable()
