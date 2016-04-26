# 7.7. Capturing Variables in Anonymous Functions


funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))

funcs2 = [lambda x, n=n: x + n for n in range(5)]
for f in funcs2:
    print(f(0))
