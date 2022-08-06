import functools
from engine.resource import resource
from engine.scene import Scene, SceneSignal
from engine.font import Font
from engine.button import Button


def init(self):

    resource.add_font("Retro_Gaming", "assets/Retro_Gaming.ttf", 28)
    font = Font(resource.font("Retro_Gaming"))
    font.set_string("I am Scene 1")
    self.add_surface(font)
    font.set_position(100, 50)

    resource.add_surface("button_idle", "assets/start_btn_c1.png")
    resource.add_surface("button_push", "assets/start_btn_c2.png")
    button = Button("change_button", resource.surface("button_idle"))
    button.set_push_img(resource.surface("button_push"))
    button.set_position(128, 120)
    button.activeOnRelease = True
    self.add_surface(button)

    def _button_pushed_on_scene(self, *args):
        self.changeScene = True
    self._button_pushed_on_scene = _button_pushed_on_scene

    self.link(button.signals.get("pushed"), self, _button_pushed_on_scene)
    self.changeScene = False


def process(self, delta: int) -> SceneSignal:
    if self.changeScene:
        ss = SceneSignal()
        ss.changeScene = True
        ss.name = "scene2"
        ss.reset = True
        return ss


def reset(self):
    self.changeScene = False


scene1 = Scene()
scene1.init = functools.partial(init, scene1)
scene1.process = functools.partial(process, scene1)
scene1.reset = functools.partial(reset, scene1)
