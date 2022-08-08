import pygame
from .lib import num
from .lib.grid import GridInt
from .lib.vect import Vec2i
from .sufaceItem import SurfaceItem


class TileMap(SurfaceItem):
    grid: GridInt
    dirty_grid: GridInt

    tileSize: int

    tileSheet: pygame.Surface
    _Hframes: int
    _Vframes: int
    _max_frame: int

    _frame: int
    _frame_coords: Vec2i
    _frame_rect_size: Vec2i

    def __init__(self, x: int, y: int, tileSize: int = 16):
        super().__init__()
        self.tileSize = tileSize
        self.grid = GridInt(Vec2i(x, y))
        self.grid.reset(-1)
        self.dirty_grid = GridInt(Vec2i(x, y))
        self.grid.reset(0)
        self.new(x * tileSize, y * tileSize)

    def load_sheet(self, s: pygame.Surface):
        self.tileSheet = s

    def set_sheetHV(self, h: int, v: int):
        '''Should load sheet surface first'''
        self._Hframes = max(1, h)
        self._Vframes = max(1, v)
        self._max_frame = self._Hframes * self._Vframes - 1
        rect_size_x = self.tileSheet.get_width() // self._Hframes
        rect_size_y = self.tileSheet.get_height() // self._Vframes
        self._frame_rect_size = Vec2i(rect_size_x, rect_size_y)
        self.size = pygame.Rect((0, 0), (rect_size_x, rect_size_y))

    def set_map(self, x: int, y: int, v: int):
        self.grid.set_grid(x, y, v)
        self.dirty_grid.set_grid(x, y, 1)

    def set_map_by_sheet_xy(self, x: int, y: int, vec: Vec2i):
        v = vec.x + vec.y * self._Hframes
        self.set_map(x, y, v)

    def update_surface(self):
        for idx, tile in enumerate(self.grid.arr):
            if self.dirty_grid.arr[idx] == 0:
                continue
            self.dirty_grid.arr[idx] = 0
            loc = self.grid.loc_from_idx(idx)
            sheet_rect = self._rect_from_frame(tile)
            sur_rect = self._rect_to_surface(loc.x, loc.y)
            self.surface.blit(self.tileSheet, sur_rect, sheet_rect)

    def _rect_to_surface(self, x: int, y: int) -> pygame.Rect:
        sx = x * self.tileSize
        sy = y * self.tileSize
        return pygame.Rect(sx, sy, sx + self.tileSize, sy + self.tileSize)

    def _rect_from_coords(self, x: int, y: int) -> pygame.Rect:
        x = num.clip(x, 0, self._Hframes - 1)
        y = num.clip(y, 0, self._Vframes - 1)
        rx = x * self._frame_rect_size.x
        ry = y * self._frame_rect_size.y
        return pygame.Rect(rx, ry, self._frame_rect_size.x, self._frame_rect_size.y)

    def _rect_from_frame(self, frame: int) -> pygame.Rect:
        frame = min(frame, self._max_frame)
        y: int = frame // self._Hframes
        x: int = frame % self._Hframes
        return self._rect_from_coords(x, y)
