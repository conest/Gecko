from __future__ import annotations
from array import array
from .vect import Vec2i


class GridInt:

    arr: array
    _size: Vec2i

    def __init__(self, size: Vec2i) -> None:
        self._size = size
        self.arr = array('i')
        for _ in range(self.length()):
            self.arr.append(0)

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.get(key[0], key[1])

    def __setitem__(self, key: tuple[int, int], value: int) -> int:
        return self.set_grid(key[0], key[1], value)

    def _idx(self, x: int, y: int) -> int:
        return self._size.x * y + x

    def size(self) -> Vec2i:
        return self._size

    def length(self) -> int:
        return self._size.volume()

    def reset(self, nInt: int):
        for i in range(self.arr):
            self.arr[i] = nInt
	
    def set_grid(self, x: int, y: int, v: int):
        self.arr[self._idx(x, y)] = v

    def get(self, x: int, y: int) -> int:
        return self.arr[self._idx(x, y)]

    # Genarate unique ID
    def pairing_id(self, x: int, y: int) -> int:
        return ( x + y ) * ( x + y + 1 ) / 2 + y

    # Check if a position in this grid
    def in_grid(self, x: int, y: int) -> bool:
        if (x < 0 or y < 0):
            return False
        if (x >= self._size.x or y >= self._size.y):
            return False
        return True

    def duplicate(self) -> GridInt:
        newGrid = GridInt(self._size.duplicate())
        for i in range(self.length()):
            newGrid.arr[i] = self.arr[i]
        return newGrid
