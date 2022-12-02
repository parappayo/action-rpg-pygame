import pygame


subscribers = []


def handle_events(world):
    """update the given sim world from the current pygame input events"""
    events = pygame.event.get()
    pressed_keys = pygame.key.get_pressed()
    for event_handlers in subscribers:
        for event in events:
            if event.type in event_handlers:
                event_handlers[event.type](event, world)
        if "pressed_keys" in event_handlers:
            event_handlers["pressed_keys"](pressed_keys, world)
