element_count = int(input("Обозначьте количество элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите следующй элемент списка "))
    i += 1

for i in range(int(len(my_list) / 2)):
    my_list[element], my_list[element + 1] = my_list[element + 1], my_list[element]
    element += 2
print(my_list)
