from sys import argv

script_name, count_hour, pay_hour, benefit = argv

calc = (int(count_hour) * int(pay_hour)) + benefit
print(f'Your salary = {calc}')
