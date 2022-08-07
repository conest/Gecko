from __future__ import annotations

from enum import Enum, auto
from .vect import Vec2i


class Direction(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()


DIR_LOC = {
    Direction.UP: (0, -1),
    Direction.DOWN: (0, 1),
    Direction.LEFT: (-1, 0),
    Direction.RIGHT: (1, 0),
}


LOC_DIR = {
    (0, -1): Direction.UP,
    (0, 1): Direction.DOWN,
    (-1, 0): Direction.LEFT,
    (1, 0): Direction.RIGHT,
}


class TilePos(Vec2i):

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return f'[TilePos] (x: {self.x}, y: {self.y})'

    def direct(self, d: Direction) -> TilePos:
        loc = DIR_LOC[d]
        return TilePos(self.x, self.y) + TilePos(loc[0], loc[1])

    def direction_from(self, toTile: TilePos) -> Direction:
        x = toTile.x - self.x
        y = toTile.y - self.y
        if (x, y) in LOC_DIR:
            return LOC_DIR[(x, y)]
        return None
