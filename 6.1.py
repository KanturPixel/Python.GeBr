from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color(('Red', 7), ('Yellow', 2), ('Green', 8))

    def lightning(self):
        for color, sec in cycle(self.__color):
            print(color, 'wait {} sec'.format(sec))
            sleep(sec)


traffic_light = TrafficLight()

