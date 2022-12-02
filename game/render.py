import pygame
from . import config
from . import sprites


def create_surface(caption):
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(config.screen_size)


def draw_texture(surface, texture_name, position):
    texture = sprites.get_texture(texture_name)
    dest_rect = texture.get_rect().move(*position)
    surface.blit(texture, dest_rect)


def draw_player(surface, player):
    draw_texture(surface, "player", player.position)


def draw_frame(surface, world):
    """render the given game sim world to the given graphics surface"""
    surface.fill(world.background_colour)

    draw_player(surface, world.player)

    pygame.display.flip()
