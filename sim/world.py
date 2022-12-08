from . import player


class World:
    def __init__(self):
        self.background_colour = 0, 0, 0  # rgb 256
        self.quit_flag = False  # set to True if the player tries to quit

        self.player = player.Player()

    def tick(self, elapsed):
        self.player.tick(elapsed)
