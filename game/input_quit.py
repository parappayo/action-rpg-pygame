import pygame
from . import input


def on_quit(event, world):
    world.quit_flag = True


def on_key_down(event, world):
    if event.key == pygame.K_ESCAPE:
        world.quit_flag = True


input.subscribers.append({
        pygame.QUIT: on_quit,
        pygame.KEYDOWN: on_key_down
    })
