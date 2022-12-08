

one_div_sqrt2 = 1 / 1.41421356237


class Player:
    def __init__(self):
        self.position = (0, 0)
        self.speed = 0.25
        self.movement_input = (0, 0)

    def velocity(self):
        if self.movement_input[0] != 0 and self.movement_input[1] != 0:
            return (
                self.movement_input[0] * self.speed * one_div_sqrt2,
                self.movement_input[1] * self.speed * one_div_sqrt2)
        return (
            self.movement_input[0] * self.speed,
            self.movement_input[1] * self.speed)

    def tick(self, elapsed):
        print(elapsed)
        velocity = self.velocity()
        velocity = (velocity[0] * elapsed, velocity[1] * elapsed)
        self.position = (
            self.position[0] + velocity[0],
            self.position[1] + velocity[1])
