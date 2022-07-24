#! /usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import engine
# from example_animation import gameScene
from example_text_button import gameScene


def main():
    engine.main.default_init()

    gameScene.init(gameScene)

    engine.main.load_scene(gameScene)
    engine.main.run()


if __name__ == "__main__":
    main()
