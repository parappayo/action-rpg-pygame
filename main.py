import game.input
import game.render
import pygame
from sim.world import World
import sys

# fixed fps makes the world update more deterministic,
# but graphics more jittery
use_fixed_fps = False
ms_per_frame = 1000 / 80


def fixed_fps_game_loop(surface, world):
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
        # print("fps: " + str(1000.0 / elapsed))

        while elapsed >= ms_per_frame:
            elapsed -= ms_per_frame
            world.tick(ms_per_frame)

        game.render.draw_frame(surface, world)


def game_loop(surface, world):
    last_update = pygame.time.get_ticks()
    elapsed = 0

    last_update = pygame.time.get_ticks()
    elapsed = ms_per_frame

    while True:
        game.input.handle_events(world)
        if world.quit_flag:
            sys.exit()

        elapsed = pygame.time.get_ticks() - last_update
        last_update = pygame.time.get_ticks()
        # print("fps: " + str(1000.0 / elapsed))

        world.tick(elapsed)
        game.render.draw_frame(surface, world)
        pygame.time.wait(1)


if __name__ == '__main__':
    surface = game.render.create_surface("Action RPG")
    world = World()

    if use_fixed_fps:
        fixed_fps_game_loop(surface, world)
    else:
        game_loop(surface, world)
