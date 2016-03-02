from Utils.utils import PropDict


class A(object):
    def __init__(self):
        self.a = 1

    def post(self):
        args = PropDict(dict(x=2, y=3))
        getattr(self, args.y)


a = A()
getattr(a, 'y')
