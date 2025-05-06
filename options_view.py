import arcade
from arcade.gui import UIManager, UITextureButton, UIAnchorLayout
# from PIL import Image

TEX_RED_BUTTON_NORMAL = arcade.load_texture(":resources:gui_basic_assets/button/red_normal.png")
TEX_RED_BUTTON_HOVER = arcade.load_texture(":resources:gui_basic_assets/button/red_hover.png")
TEX_RED_BUTTON_PRESS = arcade.load_texture(":resources:gui_basic_assets/button/red_press.png")


class OptionsView(arcade.View):
    def __init__(self, manager):
        super().__init__()

        self.manager = manager
        self.ui = None
        self.sprite_list = None
        self.analfin = None
        self.analfin_image = None
        self.body = None
        self.body_image = None
        self.dorsalfin = None
        self.dorsalfin_image = None
        self.jaw = None
        self.jaw_image = None
        self.left_eye = None
        self.left_eye_image = None
        self.right_eye = None
        self.right_eye_image = None
        self.pectoralfin = None
        self.pectoralfin_image = None
        self.tail = None
        self.tail_image = None
        self.list_colors = None

        self.setup()

    def setup(self):
        self.ui = UIManager()

        self.sprite_list = arcade.SpriteList()
        self.analfin = self.manager.analfin
        self.analfin_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.analfin}/anal_fin.png", 332/1020)
        self.body = self.manager.body
        self.body_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.body}/body.png", 332/1020)
        self.dorsalfin = self.manager.dorsalfin
        self.dorsalfin_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.dorsalfin}/dorsal_fin.png", 332/1020)
        self.jaw = self.manager.jaw
        self.jaw_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.jaw}/jaw.png", 332/1020)
        self.left_eye = self.manager.left_eye
        self.left_eye_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.left_eye}/left_eye_open.png", 332/1020)
        self.right_eye = self.manager.right_eye
        self.right_eye_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.right_eye}/right_eye_open.png", 332/1020)
        self.pectoralfin = self.manager.pectoralfin
        self.pectoralfin_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.pectoralfin}/pectoral_fin.png", 332/1020)
        self.tail = self.manager.tail
        self.tail_image = arcade.Sprite(f"./assets/2dfish/body_parts_and_spriter_file/{self.tail}/tail.png", 332/1020)

        self.list_colors = ["black", "green", "purple", "red", "yellow"]

        # Create an anchor layout, which can be used to position widgets on screen

        anchor = self.ui.add(UIAnchorLayout())

        # Add a button switch to the other View.
        button_back = anchor.add(
            UITextureButton(text="Back", width=300, texture=TEX_RED_BUTTON_NORMAL, texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-100)

        button_back_analfin = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-150, anchor_x="center",
            align_x=-140)
        button_forward_analfin = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-150, anchor_x="center",
            align_x=140)

        button_back_body = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-180, anchor_x="center",
            align_x=-140)
        button_forward_body = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-180, anchor_x="center",
            align_x=140)

        button_back_dorsalfin = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-210, anchor_x="center",
            align_x=-140)
        button_forward_dorsalfin = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-210, anchor_x="center",
            align_x=140)

        button_back_jaw = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-240, anchor_x="center",
            align_x=-140)
        button_forward_jaw = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-240, anchor_x="center",
            align_x=140)

        button_back_left_eye = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-270, anchor_x="center",
            align_x=-140)
        button_forward_left_eye = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-270, anchor_x="center",
            align_x=140)

        button_back_right_eye = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-300, anchor_x="center",
            align_x=-140)
        button_forward_right_eye = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-300, anchor_x="center",
            align_x=140)

        button_back_pectoralfin = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-330, anchor_x="center",
            align_x=-140)
        button_forward_pectoralfin = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-330, anchor_x="center",
            align_x=140)

        button_back_tail = anchor.add(
            UITextureButton(text="<", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-360, anchor_x="center",
            align_x=-140)
        button_forward_tail = anchor.add(
            UITextureButton(text=">", width=25, height=25, texture=TEX_RED_BUTTON_NORMAL,
                            texture_hovered=TEX_RED_BUTTON_HOVER,
                            texture_pressed=TEX_RED_BUTTON_PRESS), anchor_y="center", align_y=-360, anchor_x="center",
            align_x=140)

        @button_back.event("on_click")
        def on_click(event):
            self.manager.switch_to_main_menu()

        @button_back_analfin.event("on_click")
        def on_click(event):
            self.change_analfin(-1)

        @button_forward_analfin.event("on_click")
        def on_click(event):
            self.change_analfin(+1)

        @button_back_body.event("on_click")
        def on_click(event):
            self.change_body(-1)

        @button_forward_body.event("on_click")
        def on_click(event):
            self.change_body(+1)

        @button_back_dorsalfin.event("on_click")
        def on_click(event):
            self.change_dorsalfin(-1)

        @button_forward_dorsalfin.event("on_click")
        def on_click(event):
            self.change_dorsalfin(+1)

        @button_back_jaw.event("on_click")
        def on_click(event):
            self.change_jaw(-1)

        @button_forward_jaw.event("on_click")
        def on_click(event):
            self.change_jaw(+1)

        @button_back_left_eye.event("on_click")
        def on_click(event):
            self.change_left_eye(-1)

        @button_forward_left_eye.event("on_click")
        def on_click(event):
            self.change_left_eye(+1)

        @button_back_right_eye.event("on_click")
        def on_click(event):
            self.change_right_eye(-1)

        @button_forward_right_eye.event("on_click")
        def on_click(event):
            self.change_right_eye(+1)

        @button_back_pectoralfin.event("on_click")
        def on_click(event):
            self.change_pectoralfin(-1)

        @button_forward_pectoralfin.event("on_click")
        def on_click(event):
            self.change_pectoralfin(+1)

        @button_back_tail.event("on_click")
        def on_click(event):
            self.change_tail(-1)

        @button_forward_tail.event("on_click")
        def on_click(event):
            self.change_tail(+1)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()

        self.ui.draw()
        OptionsView.text_draw()

    @staticmethod
    def text_draw():
        affichage = arcade.Text("Anal Fin", align="center", x=1164/2, y=232, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Body", align="center", x=1164 / 2, y=202, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Dorsal Fin", align="center", x=1164 / 2, y=172, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Jaw", align="center", x=1164 / 2, y=142, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Left Eye", align="center", x=1164 / 2, y=112, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Right Eye", align="center", x=1164 / 2, y=82, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Pectoral Fin", align="center", x=1164 / 2, y=52, color=arcade.color.BARBIE_PINK)
        affichage.draw()
        affichage = arcade.Text("Tail", align="center", x=1164 / 2, y=22, color=arcade.color.BARBIE_PINK)
        affichage.draw()

    def change_analfin(self, direction):
        current_index = self.list_colors.index(self.analfin)
        new_index = (current_index + direction) % len(self.list_colors)
        self.analfin = self.list_colors[new_index]
        self.analfin_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.analfin}/anal_fin.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_body(self, direction):
        current_index = self.list_colors.index(self.body)
        new_index = (current_index + direction) % len(self.list_colors)
        self.body = self.list_colors[new_index]
        self.body_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.body}/body.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_dorsalfin(self, direction):
        current_index = self.list_colors.index(self.dorsalfin)
        new_index = (current_index + direction) % len(self.list_colors)
        self.dorsalfin = self.list_colors[new_index]
        self.dorsalfin_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.dorsalfin}/dorsal_fin.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_jaw(self, direction):
        current_index = self.list_colors.index(self.jaw)
        new_index = (current_index + direction) % len(self.list_colors)
        self.jaw = self.list_colors[new_index]
        self.jaw_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.jaw}/jaw.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_left_eye(self, direction):
        current_index = self.list_colors.index(self.left_eye)
        new_index = (current_index + direction) % len(self.list_colors)
        self.left_eye = self.list_colors[new_index]
        self.left_eye_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.left_eye}/left_eye_open.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_right_eye(self, direction):
        current_index = self.list_colors.index(self.right_eye)
        new_index = (current_index + direction) % len(self.list_colors)
        self.right_eye = self.list_colors[new_index]
        self.right_eye_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.right_eye}/right_eye_open.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_pectoralfin(self, direction):
        current_index = self.list_colors.index(self.pectoralfin)
        new_index = (current_index + direction) % len(self.list_colors)
        self.pectoralfin = self.list_colors[new_index]
        self.pectoralfin_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.pectoralfin}/pectoral_fin.png",
            332 / 1020
        )
        self.reset_sprites()

    def change_tail(self, direction):
        current_index = self.list_colors.index(self.tail)
        new_index = (current_index + direction) % len(self.list_colors)
        self.tail = self.list_colors[new_index]
        self.tail_image = arcade.Sprite(
            f"./assets/2dfish/body_parts_and_spriter_file/{self.tail}/tail.png",
            332 / 1020
        )
        self.reset_sprites()

    def reset_sprites(self):
        self.sprite_list.clear()
        self.dorsalfin_image.center_x = 602
        self.dorsalfin_image.center_y = 693
        self.sprite_list.append(self.dorsalfin_image)
        self.tail_image.center_x = 807
        self.tail_image.center_y = 532
        self.sprite_list.append(self.tail_image)
        self.left_eye_image.center_x = 446
        self.left_eye_image.center_y = 637
        self.sprite_list.append(self.left_eye_image)
        self.analfin_image.center_x = 725
        self.analfin_image.center_y = 459
        self.sprite_list.append(self.analfin_image)
        self.body_image.center_x = 576
        self.body_image.center_y = 566
        self.sprite_list.append(self.body_image)
        self.right_eye_image.center_x = 476
        self.right_eye_image.center_y = 636
        self.sprite_list.append(self.right_eye_image)
        self.pectoralfin_image.center_x = 645
        self.pectoralfin_image.center_y = 454
        self.sprite_list.append(self.pectoralfin_image)
        self.jaw_image.center_x = 443
        self.jaw_image.center_y = 481
        self.sprite_list.append(self.jaw_image)

    def on_show_view(self) -> None:
        self.ui.enable()
        self.reset_sprites()

    def on_hide_view(self) -> None:
        self.ui.disable()
