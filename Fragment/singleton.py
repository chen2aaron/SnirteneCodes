class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1
    b = 2


class OtherClass(object):
    a = 1
    b = 2


m = MyClass()
n = MyClass()
o = OtherClass()
p = OtherClass()


print(m._instance)
print(n._instance)
print(o)
print(p)
