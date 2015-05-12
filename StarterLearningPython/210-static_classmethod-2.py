class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod():
        print('Static:')

    @classmethod
    def cmethod(where):
        print('Class:', where)


ik = Kls(23)
ik.printd()
ik.smethod()
ik.cmethod()
# Kls.printd()   #一般方法必须用通过绑定实例调用
Kls.smethod()
Kls.cmethod()
# ik.data()

