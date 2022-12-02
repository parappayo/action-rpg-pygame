import game.input
import game.render
import pygame
from sim.world import World
import sys


if __name__ == '__main__':
    ms_per_frame = 20  # 50 fps
    surface = game.render.create_surface("Action RPG")
    world = World()

    last_update = pygame.time.get_ticks()
    elapsed = ms_per_frame

    while True:
        while elapsed < ms_per_frame:
            game.input.handle_events(world)
            if world.quit_flag:
                sys.exit()
            pygame.time.wait(1)
            elapsed = pygame.time.get_ticks() - last_update

        last_update = pygame.time.get_ticks()

        while elapsed >= ms_per_frame:
            elapsed -= ms_per_frame
            world.tick()

        game.render.draw_frame(surface, world)
