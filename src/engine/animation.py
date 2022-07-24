from enum import Enum, auto
import pygame


class Status(Enum):
    PLAY = auto()
    PAUSE = auto()
    STOP = auto()


class Frame:
    rect: pygame.Rect
    duration: int  # milliseconds

    def __init__(self, rect: pygame.Rect, duration: float):
        self.rect = rect
        self.duration = duration


class Animation:
    frames: list
    repeat: bool
    fIndex: int
    '''Index of current frame'''
    time: int
    '''Milliseconds passed since last frame played'''

    def __init__(self, repeat: bool = True):
        self.frames = []
        self.repeat = repeat
        self.fIndex = 0
        self.time = 0

    def add_frame(self, frame: Frame):
        self.frames.append(frame)

    def update(self, alpha: int) -> bool:
        '''Return True if finished'''
        self.time += alpha
        duration = self.frames[self.fIndex].duration

        while (self.time >= duration):
            # Next frame
            self.time -= duration
            if self.fIndex >= len(self.frames) - 1:
                self.fIndex = 0
                if not self.repeat:
                    self.stop()
                    return True
            else:
                self.fIndex += 1
                duration = self.frames[self.fIndex].duration

        return False

    def rect(self) -> pygame.Rect:
        return self.frames[self.fIndex].rect

    def play(self):
        pass

    def stop(self):
        self.fIndex = 0
        self.time = 0


class AnimationGroup:
    animations: dict
    '''Class[Animation] dict {Str: Animation}'''
    select: str
    '''Name of selected animation'''
    status: Status

    def __init__(self):
        self.animations = {}
        self.select = None
        self.status = Status.STOP

    def add(self, name: str, animation: Animation):
        self.animations[name] = animation

    def check(self, name: str) -> bool:
        return (name in self.animations)

    def play(self, name: str):
        if (self.status == Status.PLAY or self.status == Status.PAUSE):
            self.animations[self.select].stop()
        if (name not in self.animations):
            return
        self.select = name
        self.status = Status.PLAY
        self.animations[self.select].play()

    def stop(self):
        self.status = Status.STOP

    def pause(self):
        self.status = Status.PAUSE

    def rect(self) -> pygame.Rect:
        return self.animations[self.select].rect()

    def update(self, alpha: int):
        assert(self.select), "No animation select or loaded!"
        if self.status == Status.PAUSE:
            return
        finished = self.animations[self.select].update(alpha)
        if finished:
            self.pause()
