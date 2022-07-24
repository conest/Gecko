import os.path
import pygame


class Resource:
    _surfaces: dict
    _fonts: dict
    _sounds: dict

    def __init__(self):
        self._surfaces = {}
        self._fonts = {}
        self._sounds = {}

    def _check_path(self, path: str):
        assert(os.path.exists(path)), f"File load failed. [{path}]"

    def surface(self, name: str) -> pygame.Surface:
        return self._surfaces[name]

    def add_surface(self, name: str, path: str, convertAlpha: bool = True):
        self._check_path(path)
        # TODO: Check name duplicate
        self._surfaces[name] = pygame.image.load(path)
        if convertAlpha:
            self._surfaces[name] = self._surfaces[name].convert_alpha()

    def font(self, name: str) -> pygame.font.Font:
        return self._fonts[name]

    def add_font(self, name: str, path: str, size: int):
        self._check_path(path)
        # TODO: Check name duplicate
        self._fonts[name] = pygame.font.Font(path, size)


resource = Resource()
