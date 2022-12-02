import game.input
import game.render
from sim.world import World
import sys
import time


if __name__ == '__main__':
    surface = game.render.create_surface("Action RPG")

    world = World()

    while True:
        game.input.handle_events(world)
        if world.quit_flag:
            sys.exit()
        game.render.draw_frame(surface, world)
        time.sleep(0.001)
