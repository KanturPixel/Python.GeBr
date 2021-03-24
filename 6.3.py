class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income.wage = income['wage']
        self._income.bonus = income['bonus']

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income.wage['wage'] + self._income.bonus['bonus']


worker1 = Position('John', 'Johnson', 'driver', {"wage": 500, "bonus": 300})
print(worker1.get_full_name())
print(worker1.get_total_income())





