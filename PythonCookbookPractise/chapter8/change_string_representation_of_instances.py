# 8.1. Changing the String Representation of Instances


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

        # 0 is self, or you can use
        # return 'Pair(%r, %r)' % (self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 5)
