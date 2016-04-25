# 4.14. Flattening a Nested Sequence

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):
            yield from flatten(i)
            # or you can do this:
            # for x in flatten(i):
            #     yield x
        else:
            yield i


if __name__ == '__main__':
    item_list = [[1, 2, range(4, 10, 2)], ['hello', 'world', ['holy', 'saint']]]
    print(list(flatten(item_list)))
