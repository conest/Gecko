from engine.resource import resource
from engine.scene import Scene
from engine.sprite import AnimatedSprite
from engine.animation import Frame, Animation


def init(self):
    resource.add_surface("duck", "assets/duck.png")

    duck = AnimatedSprite(resource.surface("duck"))
    duck.set_framesHV(15, 17)
    duck.set_position(64, 64)
    self.add_surface(duck)

    animate = Animation(True)
    animate.add_frame(Frame(duck.rect_from_coords(0, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(1, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(2, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(3, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(4, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(5, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(6, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(7, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(8, 12), 100))
    animate.add_frame(Frame(duck.rect_from_coords(9, 12), 100))

    duck.animation.add("go", animate)
    duck.animation.play("go")

    # More elegant way to load Frames
    duck2 = AnimatedSprite(resource.surface("duck"))
    duck2.set_framesHV(15, 17)
    duck2.set_position(100, 100)
    self.add_surface(duck2)

    frames: list = [
        (0, 13, 150), (1, 13, 150), (2, 13, 150), (3, 13, 150),
        (4, 13, 150), (5, 13, 150), (6, 13, 150), (7, 13, 150),
        (8, 13, 150), (9, 13, 150), (10, 13, 150), (11, 13, 150),
        (12, 13, 150), (13, 13, 150), (13, 13, 150)]

    duck2.animation.add("sleep", Animation(True))
    duck2.animation_bunch_frame_load("sleep", frames)
    duck2.animation.play("sleep")


gameScene = Scene()
gameScene.init = init
