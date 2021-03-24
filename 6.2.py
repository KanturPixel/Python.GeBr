class Road:
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

    def masses(self):
        mass = self.length * self.width * 25 * 5 / 100
        return mass


road1 = Road(25, 200)
print(road1.masses())
