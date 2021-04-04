from functools import reduce


def fact(num):
    count = 1
    while count <= num:
        yield count
        count += 1


i = 1
my_fact = []
for el in fact(4):
    my_fact.append(el)
    i += 1
print(my_fact)
print(reduce(lambda x, y: x * y, my_fact))





