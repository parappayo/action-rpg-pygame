import pygame
from . import input


def on_pressed_keys(pressed_keys, world):
    x, y = 0, 0
    if pressed_keys[pygame.K_LEFT]:
        x -= 5
    if pressed_keys[pygame.K_RIGHT]:
        x += 5
    if pressed_keys[pygame.K_UP]:
        y -= 5
    if pressed_keys[pygame.K_DOWN]:
        y += 5
    world.player.velocity = (x, y)


input.subscribers.append({
        "pressed_keys": on_pressed_keys
    })
