import pygame
from . import config
from . import sprites


def create_surface(caption):
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(config.screen_size)


def draw_frame(surface, world):
    """render the given game sim world to the given graphics surface"""
    surface.fill(world.background_colour)

    draw_texture(surface, "player")

    pygame.display.flip()


def draw_texture(surface, texture_name):
    texture = sprites.get_texture(texture_name)
    surface.blit(texture, texture.get_rect())
