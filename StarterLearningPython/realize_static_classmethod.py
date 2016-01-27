class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        print('Static:', arg)

    @classmethod
    def cmethod(*arg):
        print('Class:', *arg)


c = Kls(20)
print('-'*10)
c.printd()
c.smethod(20)
c.cmethod()
Kls.smethod(20)
Kls.cmethod()
# print(Kls.printd())
# print('-'*10)
# print(c.smethod())
# print(Kls.smethod())
# print('-'*10)
# print(c.cmethod())
# print(Kls.cmethod())
