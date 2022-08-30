import functools
from engine.resource import resource
from engine.scene import Scene
from engine.tilemap import TileMap
from engine.lib.vect import Vec2i


def init(self):
    resource.add_surface("duck", "assets/duck.png")

    tileMap = TileMap(3, 3, 32)
    tileMap.load_sheet(resource.surface("duck"))
    tileMap.set_sheetHV(15, 17)
    tileMap.set_position(64, 64)

    tileMap.set_map(1, 1, 0)
    tileMap.set_map_by_sheet_xy(0, 0, Vec2i(4, 11))
    tileMap.set_map_by_sheet_xy(2, 2, Vec2i(8, 12))

    tileMap.update_surface()
    self.surfaceList.add(tileMap)


gameScene = Scene()
gameScene.init = functools.partial(init, gameScene)
