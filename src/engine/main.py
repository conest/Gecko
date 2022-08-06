import pygame
from .scene import Scene, SceneSignal

BACKGROUND_COLOR = pygame.Color(128, 128, 128)


class Engine:
    _inited: bool = False
    screen: pygame.Surface
    fpsLimit: int = 60
    scene: Scene = None
    sceneDic: dict = {}

    def inited(self) -> bool:
        return self._inited

    def init(self, windowSize: tuple, flag: int, caption: str, vsync: int = 1):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(windowSize, flag, vsync=vsync)
        self.sceneDic = {}
        self._inited = True

    def default_init(self):
        WINDOW_SIZE = (800, 450)
        WINDOW_FLAG = pygame.RESIZABLE | pygame.SCALED
        WINDOW_CAPTION = "My Awesome Game"
        self.init(WINDOW_SIZE, WINDOW_FLAG, WINDOW_CAPTION, vsync=1)

    def set_fps(self, fps: int):
        self.fpsLimit = fps

    def add_scene(self, s: Scene, name: str):
        self.sceneDic[name] = s

    def load_scene(self, s: Scene, name: str = "entry"):
        self.scene = s
        self.add_scene(s, name)

    def _handle_scene(self, ss: SceneSignal) -> bool:
        if ss is None:
            return True
        if ss.endGame:
            return False
        if ss.changeScene:
            scene = self.sceneDic[ss.name]
            if ss.reset:
                scene.reset()
        return True

    def run(self):
        assert(self._inited), "Engine must be initialized first!"
        assert(self.scene), "A scene must be loaded!"

        fps = pygame.time.Clock()
        running = True
        scene = self.scene

        while running:
            delta: int = fps.tick(self.fpsLimit)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                scene.event_handle(event, delta)

            scene.update(delta)
            ss: SceneSignal = scene.process(delta)
            scene.signal_handle()

            self.screen.fill(BACKGROUND_COLOR)
            scene.draw(self.screen)
            pygame.display.update()

            if not self._handle_scene(ss):
                running = False


engine = Engine()
