import pygame
from pygame import Surface

from .surfaceItem import SurfaceItem, SurfaceList
from .lib.vect import Vec2i, Vec2f
from .lib.num import clip


FOCUS_SIZE_RATIO = 3


class Camera(SurfaceItem):
    mag: int
    '''Magnification'''
    cPositon: Vec2f
    '''Camera Position'''
    source: SurfaceItem
    sourceSize: Vec2i
    border: bool
    '''Restrict the camera in the source's surface'''
    cutSize: Vec2i
    focusSize: Vec2i

    def __init__(self, cameraSize: Vec2i, mag: int = 1, border: bool = False):
        super().__init__()
        self.name = "Camera"
        self.new(cameraSize.x, cameraSize.y)
        self.set_mag(mag)
        self.cPositon = Vec2f()
        self.border = border

    def set_mag(self, mag: int = 1):
        if mag <= 0:
            mag = 1
        self.mag = mag
        self.cutSize = Vec2i(int(self.size.w / self.mag), int(self.size.h / self.mag))
        self.focusSize = self.cutSize / FOCUS_SIZE_RATIO

    def load_source(self, si: SurfaceItem):
        self.source = si
        self.sourceSize = Vec2i(si.size.w, si.size.h)

    def move_to(self, x: float, y: float):
        self.cPositon.x = x
        if self.border:
            top = self.sourceSize.x - self.cutSize.x
            self.cPositon.x = clip(self.cPositon.x, 0, top)

        self.cPositon.y = y
        if self.border:
            top = self.sourceSize.y - self.cutSize.y
            self.cPositon.y = clip(self.cPositon.y, 0, top)

        self.update_surface()

    def move(self, x: float, y: float):
        self.move_to(self.cPositon.x + x, self.cPositon.y + y)

    def moveCenter(self, v: Vec2f):
        self.move_to(v.x - self.cutSize.x / 2, v.y - self.cutSize.y / 2)

    def _scale_surface(self, s: Surface, zoom: float) -> Surface:
        rect = s.get_rect()
        sizex = (rect.w * zoom, rect.h * zoom)
        return pygame.transform.scale(s, sizex)

    def update_surface(self):
        cutSize = self.cutSize.to_tuple()
        blitArea = pygame.Rect(self.cPositon.to_tuple_int(), cutSize)
        sourceCut = Surface(cutSize, pygame.SRCALPHA)
        sourceCut.blit(self.source.surface, (0, 0), blitArea)
        self.surface = self._scale_surface(sourceCut, self.mag)

    def onFocus(self, v: Vec2f):
        focusPos: Vec2i = self.cPositon.to_Vec2i() + (self.cutSize - self.focusSize) / 2
        focusRect = pygame.Rect(focusPos.to_tuple(), self.focusSize.to_tuple())
        if focusRect.collidepoint(v.x, v.y):
            return
        if v.x < focusRect.x:
            self.move(v.x - focusRect.x, 0)
        if v.x > focusRect.right:
            self.move(v.x - focusRect.right + 1, 0)
        if v.y < focusRect.y:
            self.move(0, v.y - focusRect.y)
        if v.y > focusRect.bottom:
            self.move(0, v.y - focusRect.bottom + 1)

    def camera_rect(self) -> pygame.Rect:
        return pygame.Rect(self.cPositon.to_tuple_int(), self.cutSize.to_tuple())

    def in_camera(self, rect: pygame.Rect) -> bool:
        return self.camera_rect().colliderect(rect)

    def update(self, delta: int):
        self.source.update(delta)


class CameraStack(Camera):

    sources: SurfaceList

    def __init__(self, cameraSize: Vec2i, mag: int = 1, border: bool = False):
        super().__init__(cameraSize, mag, border)
        self.sources = SurfaceList("CameraStack_sources")

    def add_source(self, si: SurfaceItem):
        self.sources.add(si)
        self.sourceSize = Vec2i(si.size.w, si.size.h)

    def update_surface(self):
        cutSize = self.cutSize.to_tuple()
        blitArea = pygame.Rect(self.cPositon.to_tuple_int(), cutSize)
        sourceCut = Surface(cutSize, pygame.SRCALPHA)

        self.sources.draw_with_area(sourceCut, blitArea)
        self.surface = self._scale_surface(sourceCut, self.mag)

    def update(self, delta: int):
        if self.sources.update(delta):
            self.update_surface()
