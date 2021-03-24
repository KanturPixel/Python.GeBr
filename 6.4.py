class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is starting'.format(self.name))

    def stop(self):
        print('{} stopped'.format(self.name))

    def turn(self, direction):
        print('{} has turned {}'.format(self.name, direction))

    def show_speed(self):
        print('Current speed of {}: {}'.format(self.name, self.speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Your speed is higher then available!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Your speed is higher then available!')


class PoliceCar(Car):
    pass

class SportCar(Car):
    pass


car1 = TownCar(80, 'green', 'Dodg', False)
car2 = TownCar(45, 'yellow', 'Caddilac', False)
car3 = PoliceCar(80, 'black', 'Ford', True)
car4 = WorkCar(90, 'Red', 'Ford', False)

car1.show_speed()
car2.turn('right')
car3.stop()
