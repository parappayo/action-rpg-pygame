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


def on_joysticks(joysticks, world):
    if len(joysticks) < 1:
        return
    # joy1 = joysticks[0]
    # print("name: " + joy1.get_name())
    # print("numaxes: " + str(joy1.get_numaxes()))
    # for i in range(joy1.get_numaxes()):
    #     print(joy1.get_axis(i))


input.subscribers.append({
        "pressed_keys": on_pressed_keys,
        "joysticks": on_joysticks,
    })
