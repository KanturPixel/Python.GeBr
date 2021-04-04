def my_sum():
    esc = False
    res = 0
    while esc == False:
        numb = input('Enter numbers or q to escape: ').split()
        res_line = 0
        for i in numb:
            if 'q' in i:
                esc = True
                break
            res_line += int(i)
        res += res_line
    return res
