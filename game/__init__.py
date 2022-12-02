# game package

import pygame
from . import input_player
from . import input_quit
from . import sprites

__all__ = ["config", "input", "render", "sprites"]

pygame.init()
sprites.load_textures()
