# 1.14. Sorting Objects Without Native Comparison Support
from operator import attrgetter


class User(object):
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'User({}, {})'.format(self.user_id, self.first_name.capitalize() + self.last_name.capitalize())


def sorted_by_lambda(users):
    return sorted(users, key=lambda u: (u.first_name, u.last_name))


def sorted_by_attrgetter(users):
    return sorted(users, key=attrgetter('first_name', 'last_name'))

if __name__ == '__main__':
    users = [
        User(2, 'wang', 'er'),
        User(5, 'chen', 'san'),
        User(8, 'li', 'si'),
        User(1, 'li', 'wu'),
        ]
    print(sorted_by_lambda(users))
    import timeit
    # Efficiency: attrgetter > lambda
    print(timeit.timeit(
        stmt="sorted_by_attrgetter(users)",
        setup="from __main__ import sorted_by_attrgetter, users",
        number=100000
    ))
    print(timeit.timeit(
        stmt="sorted_by_lambda(users)",
        setup="from __main__ import sorted_by_lambda, users",
        number=100000
    ))
