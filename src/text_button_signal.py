#! /usr/bin/env python3
import engine
from text_button_signal_scene import gameScene


def main():
    engine.main.default_init()

    gameScene.init()

    engine.main.load_scene(gameScene)
    engine.main.run()


if __name__ == "__main__":
    main()
