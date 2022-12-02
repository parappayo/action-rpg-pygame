

class Player:
    def __init__(self):
        self.position = (0, 0)
        self.velocity = (0, 0)

    def tick(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1])
