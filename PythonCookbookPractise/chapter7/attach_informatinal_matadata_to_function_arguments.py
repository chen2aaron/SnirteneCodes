# 7.3. Attaching Informational Metadata to Function Arguments


def add(x: int, y: int) -> int:
    return x + y


def a():
    return 'a'


if __name__ == '__main__':
    help(add)
    print(add.__annotations__)

    help(a)
    print(a.__annotations__)
