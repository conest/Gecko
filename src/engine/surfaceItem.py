import pygame
from .object import Object, ObjectList
from .lib.vect import Vec2f


class SurfaceItem(Object):
    '''Surface item, base class for graphic present items'''
    surface: pygame.Surface
    size: pygame.Rect
    position: Vec2f
    visible: bool
    zIndex: int

    def __init__(self):
        super().__init__()
        self.surface = None
        self.size = pygame.Rect(0, 0, 0, 0)
        self.position = Vec2f()
        self.zIndex = 0
        self.visible = True

    def new(self, x: int, y: int):
        self.surface = pygame.Surface((x, y), pygame.SRCALPHA)
        self.size = pygame.Rect(0, 0, x, y)

    def load_surface(self, s: pygame.Surface):
        self.surface = s
        self.size = pygame.Rect((0, 0), s.get_size())

    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.position.to_tuple_int(), self.size.size)

    def set_position(self, x: float, y: float):
        self.position.set(x, y)

    def set_position_v(self, v: Vec2f):
        self.position = v

    def surface_size(self) -> pygame.Rect:
        return self.surface.get_rect()

    def draw(self, surface: pygame.Surface):
        if self.visible:
            surface.blit(self.surface, self.position.to_tuple_int())

    def draw_to(self, surface: pygame.Surface, pos: Vec2f):
        if self.visible:
            surface.blit(self.surface, pos.to_tuple_int())

    def draw_directly(self, surface: pygame.Surface):
        surface.blit(self.surface, (0, 0))

    def draw_with_area(self, surface: pygame.Surface, area: pygame.Rect):
        if self.visible:
            surface.blit(self.surface, self.position.to_tuple_int(), area)


class SurfaceList(ObjectList):

    def __init__(self, groupName: str = "SurfaceGroup"):
        super().__init__(groupName)

    def update(self, delta: int) -> bool:
        '''Update surface graphic, return true if some surface changed'''
        changed = False
        for s in self.objects:
            if s.update(delta) is True:
                changed = True
        return changed

    def draw(self, screen: pygame.Surface):
        '''Draw surface graph on the screen'''
        for s in self.objects:
            s.draw(screen)

    def draw_with_area(self, screen: pygame.Surface, area: pygame.Rect):
        for s in self.objects:
            s.draw_with_area(screen, area)

    def sort(self):
        '''Sort surfaces by zIndex'''
        self.objects.sort(key=lambda s: s.zIndex)
