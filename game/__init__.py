# game package

import pygame
from . import input_quit
from . import sprites

__all__ = ["config", "input", "render"]

pygame.init()
sprites.load_textures()
