import pygame
from . import input


def on_pressed_keys(pressed_keys, world):
    x, y = 0, 0
    if pressed_keys[pygame.K_LEFT]:
        x -= 1
    if pressed_keys[pygame.K_RIGHT]:
        x += 1
    if pressed_keys[pygame.K_UP]:
        y -= 1
    if pressed_keys[pygame.K_DOWN]:
        y += 1
    world.player.movement_input = (x, y)


input.subscribers.append({
        "pressed_keys": on_pressed_keys
    })
