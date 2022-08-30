import functools
import pygame
from engine.resource import resource
from engine.scene import Scene
from engine.sprite import Sprite
from engine.font import Font
from engine.textContainer import TextContainer
from engine.button import Button


def init(self):
    resource.add_surface("sprite_sheet", "assets/dc2.png")
    sprite = Sprite(resource.surface("sprite_sheet"))
    sprite.set_framesHV(7, 2)
    sprite.set_frame(3)
    sprite.set_position(64, 64)
    self.surfaceList.add(sprite)

    resource.add_font("small_pixel", "assets/small_pixel.ttf", 8)
    font = Font(resource.font("small_pixel"))
    font.set_string("Font test AaBbCc_1234567890")
    self.surfaceList.add(font)
    font.set_position(100, 16)

    resource.add_font("Retro_Gaming", "assets/Retro_Gaming.ttf", 11)
    tc = TextContainer(pygame.Rect(0, 0, 340, 80), resource.font("Retro_Gaming"))

    # TextContainer has auto line break (only work with Roman alphabet)
    tc.add_text("Lorem ipsum dolor sit amet, consectetur \
        adipiscing elit. Praesent varius tortor et dui feugiat,\
        at consequat lectus tempus. Cras bibendum felis quis nibh\
        pulvinar viverra. In quis nisl dolor.")
    tc.set_position(30, 130)
    self.surfaceList.add(tc)

    def _button_pushed_on_tc(self, *args):
        self.buttonpushed += 1
        self.add_text(f"button pushed {self.buttonpushed} times")
    tc._button_pushed_on_tc = _button_pushed_on_tc
    tc.buttonpushed = 0

    resource.add_surface("button_idle", "assets/start_btn_s1.png")
    resource.add_surface("button_push", "assets/start_btn_s2.png")
    button = Button("start_button", resource.surface("button_idle"))
    button.set_push_img(resource.surface("button_push"))
    button.set_position(128, 64)
    self.surfaceList.add(button)

    tc._button_pushed_on_tc = functools.partial(_button_pushed_on_tc, tc)
    self.link(button.signals.get("pushed"), tc._button_pushed_on_tc)


gameScene = Scene()
gameScene.init = functools.partial(init, gameScene)
