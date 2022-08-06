#! /usr/bin/env python3
import pygame
import engine
from animation_scene import gameScene


def main():
    WINDOW_SIZE = (225, 300)
    WINDOW_FLAG = pygame.RESIZABLE | pygame.SCALED
    WINDOW_CAPTION = "Space Duck Drop!"
    engine.main.init(WINDOW_SIZE, WINDOW_FLAG, WINDOW_CAPTION)
    # engine.main.default_init()

    gameScene.init()

    engine.main.load_scene(gameScene)
    engine.main.run()


if __name__ == "__main__":
    main()
