with open('ask_4.txt', encoding='utf-8') as a:
    strings = a.readlines()

with open('rus_ask_4.txt', 'w', encoding='utf-8') as r:
    for i in strings:
        if '1' in i:
            i = i.replace('One', 'Один')
        elif '2' in i:
            i = i.replace('Two', 'Два')
        elif '3' in i:
            i = i.replace('Three', 'Три')
        elif '4' in i:
            i = i.replace('Four', 'Четыре')
        r.write(i)
