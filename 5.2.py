with open('test.txt', 'r') as t:
    strings = t.readlines()
print('Count of strings', len(strings))
for number, string in enumerate(strings, start=1):
    print('{} string contains {} words'.format(number, len(string.split())))


