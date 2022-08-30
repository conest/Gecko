from __future__ import annotations
from numbers import Number


class Vec2i:
    x: int = 0
    y: int = 0

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.set(x, y)

    def from_tuple(t: tuple[int, int]) -> Vec2i:
        return Vec2i(t[0], t[1])

    def __str__(self) -> str:
        return f'[Vec2i] (x: {self.x}, y: {self.y})'

    def __eq__(self, o: Vec2i) -> bool:
        if self.x == o.x and self.y == o.y:
            return True
        else:
            return False

    def __add__(self, o: Vec2i) -> Vec2i:
        return Vec2i(self.x + o.x, self.y + o.y)

    def __sub__(self, o: Vec2i) -> Vec2i:
        return Vec2i(self.x - o.x, self.y - o.y)

    def __mul__(self, o: Number) -> Vec2i:
        return Vec2i(self.x * o, self.y * o)

    def __truediv__(self, o: Number) -> Vec2i:
        return Vec2i(self.x / o, self.y / o)

    def __floordiv__(self, o: Number) -> Vec2i:
        return Vec2i(self.x // o, self.y // o)

    def set(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def volume(self) -> int:
        return self.x * self.y

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

    def to_Vec2f(self) -> Vec2f:
        return Vec2f(float(self.x), float(self.y))

    def distence(self, to: Vec2i) -> int:
        return abs(to.x - self.x) + abs(to.y - self.y)

    def duplicate(self) -> Vec2i:
        return Vec2i(self.x, self.y)


class Vec2f:
    x: float = 0
    y: float = 0

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.set(x, y)

    def __str__(self) -> str:
        return f'[Vec2f] (x: {self.x}, y: {self.y})'

    def from_tuple(t: tuple[float, float]) -> Vec2f:
        return Vec2f(t[0], t[1])

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

    def to_tuple_int(self) -> tuple:
        return (int(self.x), int(self.y))

    def to_Vec2i(self) -> Vec2i:
        return Vec2i(int(self.x), int(self.y))

    def __eq__(self, o) -> bool:
        if self.x == o.x and self.y == o.y:
            return True
        else:
            return False

    def __add__(self, o: Vec2f) -> Vec2f:
        return Vec2f(self.x + o.x, self.y + o.y)

    def __sub__(self, o: Vec2f) -> Vec2f:
        return Vec2f(self.x - o.x, self.y - o.y)

    def __mul__(self, o: Number) -> Vec2f:
        return Vec2f(self.x * o, self.y * o)

    def __truediv__(self, o: Number) -> Vec2f:
        return Vec2f(self.x / o, self.y / o)

    def __floordiv__(self, o: Number) -> Vec2f:
        return Vec2f(self.x // o, self.y // o)

    def set(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def move(self, x, y) -> None:
        self.x += x
        self.y += y
