profit = int(input('Введите значение выручки:'))
costs = int(input('Введите значение издержек:'))
if profit > costs:
    print(f'Фирма работает с прибылью. Рентабельность выручки составила {profit / costs}')
    workers = int(input('Введите количество сотрудников'))
    print(f'прибыль в расчете на одного сторудника сотавила {profit / workers}')

else:
    print('Ваша фирма работает в убыток')


