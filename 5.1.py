with open('test.txt', 'w') as t:
    while True:
        string = input('Enter the text: ')
        if string == '':
            break
        t.write(string + '\n')

