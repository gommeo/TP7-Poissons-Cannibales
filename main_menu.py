import arcade
from arcade.gui import UIManager, UITextureButton, UIAnchorLayout

TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")


class MainMenu(arcade.View):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.ui = None

        self.setup()

    def setup(self):
        # Create a UIManager
        self.ui = UIManager()

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())

        # Add a button switch to the other View.
        button_play = anchor.add(
            UITextureButton(
                text="Play",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",  # Adjust the vertical position here ("top", "center", "bottom")
            align_y=-25
        )
        button_highscore = anchor.add(
            UITextureButton(
                text="Highscores",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",  # Adjust the vertical position here ("top", "center", "bottom")
            align_y=-100
        )
        button_options = anchor.add(
            UITextureButton(
                text="Options",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",  # Adjust the vertical position here ("top", "center", "bottom")
            align_y=-175
        )
        button_quit = anchor.add(
            UITextureButton(
                text="Quit",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",  # Adjust the vertical position here ("top", "center", "bottom")
            align_y=-250
        )

        # add a button to switch to the blue view
        @button_play.event("on_click")
        def on_click(event):
            self.manager.switch_to_game_view()

        @button_highscore.event("on_click")
        def on_click(event):
            self.manager.switch_to_high_score_view()

        @button_options.event("on_click")
        def on_click(event):
            self.manager.switch_to_options_view()

        @button_quit.event("on_click")
        def on_click(event):
            self.manager.save_game()
            self.window.close()

    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_show(self):
        pass

    def on_draw(self):
        self.clear()

        self.ui.draw()

    def on_update(self, delta_time):
        pass
