time_before = int(input('Введите время в секундах :'))
hours = time_before // 3600
minuts = (time_before % 3600) // 60
seconds = (time_before % 3600) % 60
print(f'{hours} : {minuts} : {seconds}')
