#! /usr/bin/env python3
import engine
from scene_change_scene_1 import scene1
from scene_change_scene_2 import scene2


def main():
    engine.main.default_init()

    scene1.init()
    scene2.init()

    engine.main.load_scene(scene1)
    engine.main.add_scene(scene2, "scene2")
    engine.main.run()


if __name__ == "__main__":
    main()
