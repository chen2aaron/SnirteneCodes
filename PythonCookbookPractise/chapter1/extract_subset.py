# 1.17. Extracting a Subset of a Dictionary


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


def dict_comprehension(data):
    return {key: value for key, value in data.items() if value > 200}


def dict_func(data):
    return dict((key, value) for key, value in data.items() if value > 200)


tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p3 = {key: value for key, value in prices.items() if key in tech_names}

if __name__ == '__main__':
    import timeit
    # Efficiency: dict_comprehension > dict_func
    print(timeit.timeit(
        stmt="dict_comprehension(prices)",
        setup="from __main__ import dict_comprehension, prices",
        number=100000,
    ))
    print(timeit.timeit(
        stmt="dict_func(prices)",
        setup="from __main__ import dict_func, prices",
        number=100000,
    ))
