# 1.10. Removing Duplicates from a Sequence while Maintaining Order


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = items if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    import timeit

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(timeit.timeit("list(dedupe(b, key=lambda d: (d['x'], d['y'])))",
                        setup='from __main__ import dedupe, b',
                        number=100000))
    print(timeit.timeit('list(set(a))',
                        setup='from __main__ import a',
                        number=100000))
    print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))
    # 不能维护元素的顺序
    print(list(set(a)))