from typing import Callable
import pygame
from .sufaceItem import SurfaceItem
from .signal import Signal, Link


class Scene:
    objects: dict = {}
    '''Commen objects dic'''
    surfaceGroup: list = []
    '''SurfaceItem List'''
    links: list = []
    '''Signal links'''

    def __init__(self):
        self.surfaceGroup = []
        self.links = []

    def init(self):
        pass

    def update(self, delta: int):
        '''Update surface graphic'''
        for s in self.surfaceGroup:
            s.update(delta)

    def process(self, delta: int):
        '''Scene self logic handle'''
        pass

    def signal_handle(self):
        for link in self.links:
            if link.signal_active():
                link.call_target()

    def event_handle(self, event: pygame.event.Event, delta: int):
        pass

    def draw(self, screen: pygame.Surface):
        '''Draw surface graph on the screen'''
        for s in self.surfaceGroup:
            s.draw(screen)

    def sort_surfaces(self):
        self.surfaceGroup.sort(key=lambda s: s.zIndex)

    def add_surface(self, si: SurfaceItem, checkDup: bool = True):
        if checkDup:
            self._check_name_unique(si.name)
        self.surfaceGroup.append(si)

    def delete_surface(self, name: str) -> bool:
        '''Return False if nothing find in the list with the given name'''
        for i, o in enumerate(self.surfaceGroup):
            if o.name == name:
                del self.surfaceGroup[i]
                return True
        return False

    def _check_name_unique(self, name: str):
        for s in self.surfaceGroup:
            if s.name == name:
                print(f'[WARNING] Find surface name duplicated: {s.name}')

    def check_all_surface_name(self, logout: bool = False) -> dict:
        nameDict = {}
        for s in self.surfaceGroup:
            if s.name in nameDict:
                if logout:
                    print(f'[WARNING] Find surface name duplicated: {s.name}')
                return {'dup_name': s.name}
            else:
                nameDict[s.name] = True
        return {}

    def link(self, source: Signal, target: SurfaceItem, targetFunc: Callable):
        self.links.append(Link(source, target, targetFunc))
