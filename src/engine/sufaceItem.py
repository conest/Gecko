import pygame
from .signal import SignalGroup


class SurfaceItem:
    '''Surface item, base class for graphic present items'''
    surface: pygame.Surface
    size: pygame.Rect
    position: pygame.Rect
    visible: bool
    zIndex: int
    name: str
    '''SurfaceItem.name: work as an unique ID'''
    signals: SignalGroup

    def __init__(self):
        self.surface = None
        self.size = pygame.Rect(0, 0, 0, 0)
        self.position = pygame.Rect(0, 0, 0, 0)
        self.zIndex = 0
        self.visible = True
        self.signals = SignalGroup()

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.position.x, self.position.y, self.size.w, self.size.h)

    def set_position(self, x: float, y: float):
        self.position.x = x
        self.position.y = y

    def surface_size(self) -> pygame.Rect:
        return self.surface.get_rect()

    def draw(self, surface: pygame.Surface):
        if self.visible:
            surface.blit(self.surface, self.position)

    def update(self, _delta: int):
        pass
