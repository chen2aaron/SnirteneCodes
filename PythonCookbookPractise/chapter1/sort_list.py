# 1.13. Sorting a List of Dictionaries by a Common Key
from operator import itemgetter
from pprint import pprint


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
pprint(rows_by_fname)
pprint(rows_by_uid)
pprint(rows_by_lfname)
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))

rows_by_fname_lambda = sorted(rows, key=lambda r: (r['lname'], r['fname']))
pprint(rows_by_fname_lambda)


if __name__ == '__main__':
    import timeit
    # Efficiency: itemgetter > lambda
    print(timeit.timeit(
        stmt="sorted(rows, key=itemgetter('uid'))",
        setup="from __main__ import itemgetter, rows",
        number=100000
    ))
    print(timeit.timeit(
        stmt="sorted(rows, key=lambda r: (r['lname'], r['fname']))",
        setup="from __main__ import itemgetter, rows",
        number=100000
    ))
