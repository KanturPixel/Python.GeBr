with open('salaries.txt', encoding='utf-8') as s:
    strings = s.readlines()

salaries = []
for string in strings:
    name, salary = string.split(' - ')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(string, end=' ')
print('Average salary is ', sum(salaries) / len(salaries))
