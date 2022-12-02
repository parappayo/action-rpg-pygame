import pygame
from . import config


def create_surface(caption):
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(config.screen_size)


def draw_frame(surface, world):
    """render the given game sim world to the given graphics surface"""
    surface.fill(world.background_colour)

    # TODO: surface.blit something

    pygame.display.flip()
