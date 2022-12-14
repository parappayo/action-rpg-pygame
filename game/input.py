import pygame


subscribers = []
joysticks = []


def init_joysticks():
    global joysticks
    joysticks = [
        pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())
    ]
    if len(joysticks) > 0:
        for joy in joysticks:
            print("Detected joystick " + joy.get_name())


def handle_events(world):
    """update the given sim world from the current pygame input events"""
    events = pygame.event.get()
    pressed_keys = pygame.key.get_pressed()

    if len(joysticks) < 1:
        init_joysticks()

    for event_handlers in subscribers:
        for event in events:
            if event.type in event_handlers:
                event_handlers[event.type](event, world)
        if "pressed_keys" in event_handlers:
            event_handlers["pressed_keys"](pressed_keys, world)
        if "joysticks" in event_handlers:
            event_handlers["joysticks"](joysticks, world)


def debug_print_joy(joy):
    print("name: " + joy.get_name())
    print("numaxes: " + str(joy.get_numaxes()))
    for i in range(joy.get_numaxes()):
        print(joy.get_axis(i))


def apply_dead_zone(axis):
    if 0 < axis and axis < 0.12:
        return 0
    if -0.12 < axis and axis < 0:
        return 0
    return axis
