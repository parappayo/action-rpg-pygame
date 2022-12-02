import pygame


subscribers = []


def handle_events(world):
    """update the given sim world from the current pygame input events"""
    events = pygame.event.get()
    for event_handlers in subscribers:
        for event in events:
            if event.type not in event_handlers:
                continue
            event_handlers[event.type](event, world)
