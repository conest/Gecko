#! /usr/bin/env python3
import pygame
import engine
from scene_tilemap import gameScene


def main():
    WINDOW_SIZE = (300, 300)
    WINDOW_FLAG = pygame.RESIZABLE | pygame.SCALED
    WINDOW_CAPTION = "TileMap Example"
    engine.main.init(WINDOW_SIZE, WINDOW_FLAG, WINDOW_CAPTION)

    gameScene.init()

    engine.main.load_scene(gameScene)
    engine.main.run()


if __name__ == "__main__":
    main()
