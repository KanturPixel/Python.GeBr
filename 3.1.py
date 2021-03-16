def division(a, b):
    try:
        a, b = int(a), int(b)
        result = a/ b

    except ZeroDivisionError:
        return 'Division on Zero'
    return result


division(input(), input())
