class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):

        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):

        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):

       print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):

       print('Запуск отрисовки маркером')


penc1 = Handle('Маркер')
penc2 = Pen('Ручка')
penc3 = Pencil('Карандаш')
penc1.draw()
penc2.draw()
penc3.draw()
