import arcade
from arcade.gui import UIManager, UITextureButton, UIAnchorLayout


TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")


class PauseView(arcade.View):
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
        button_resume = anchor.add(
            UITextureButton(
                text="Resume",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",  # Adjust the vertical position here ("top", "center", "bottom")
            align_y=-75
        )

        button_return = anchor.add(
            UITextureButton(
                text="Main Menu",
                width=300,
                texture=TEX_RED_BUTTON_NORMAL,
                texture_hovered=TEX_RED_BUTTON_HOVER,
                texture_pressed=TEX_RED_BUTTON_PRESS,
            ),
            anchor_y="center",  # Adjust the vertical position here ("top", "center", "bottom")
            align_y=0
        )

        @button_resume.event("on_click")
        def on_click(event):
            self.manager.switch_to_game_view()

        @button_return.event("on_click")
        def on_click(event):
            self.manager.switch_to_main_menu()

    def on_draw(self):
        self.clear()

        self.ui.draw()

    def on_key_press(self, key, modifiers):
        if key == "esc":
            self.manager.switch_to_game_view()

    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()
