from itertools import count, cycle


for el in count(3):
    if el > 20:
        break
    else:
        print(el)

i = 0
for el in cycle('ADG'):
    if i > 20:
        break
    print(el)
    i += 1






