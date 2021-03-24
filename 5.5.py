with open('ask_5.txt', 'w') as a:
    nums = input('Enter numbers through a space: ')
    a.write('Entered numbers:' + nums + '\n')
    nums = map(int, nums.split())
    a.write('Sum of numbers: ' + str(sum(nums)))


