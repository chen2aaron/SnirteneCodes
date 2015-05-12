def func(x, *arg):
    print x
    result = x
    print arg
    for i in arg:
        result += i
    return result
print func(1, 2, 3, 4, 5, 6, 7, 8, 9)
