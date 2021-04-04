my_dict = []
with open('ask_6.txt', encoding='utf-8') as a:
    strings = a.readlines()

for i in strings:
    spl_lines = i.split()
    subj = spl_lines[0]
    sum_lessons = sum([int(x[:x.find('(')]) for x in spl_lines[1:] if '(' in x])
    my_dict[subj[:-1]] = sum_lessons

print(my_dict)




