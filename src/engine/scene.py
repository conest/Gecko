from __future__ import annotations
from typing import Callable

import pygame
from .surfaceItem import SurfaceList
from .signal import Signal, Link


class SceneSignal:
    endGame: bool = False
    changeScene: bool = False
    name: str
    reset: False


class Scene:
    objects: dict = {}
    '''Commen objects dic'''
    surfaceList: SurfaceList
    links: list[Link] = []
    '''Signal links'''

    def __init__(self):
        self.surfaceList = SurfaceList()
        self.links = []

    def init(self):
        pass

    def reset(self):
        pass

    def process(self, delta: int) -> SceneSignal:
        '''Scene self logic handle'''
        pass

    def event_handle(self, event: pygame.event.Event, delta: int):
        pass

    def signal_handle(self):
        for link in self.links:
            if link.signal_active():
                link.call_target()

    def update(self, delta: int):
        self.surfaceList.update(delta)

    def draw(self, screen: pygame.Surface):
        self.surfaceList.draw(screen)

    def link(self, source: Signal, targetFunc: Callable):
        self.links.append(Link(source, targetFunc))

    def delete_obj(self, name: str, isSurface: bool = False):
        del self.objects[name]
        if isSurface:
            self.surfaceList.delete(name)
