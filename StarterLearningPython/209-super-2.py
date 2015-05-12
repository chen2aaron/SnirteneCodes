#!/usr/bin/env python
# coding=utf-8


class Person(object):

    def __init__(self):
        self.height = 160

    def about(self, name):
        print "{} is about {}".format(name, self.height)


class Girl(Person):

    def __init__(self):
        super(Girl, self).__init__()  # 方法一
        # Person.__init__(self) # 方法二
        self.breast = 90

    def about(self, name):
        super(Girl, self).about(name)
        print "{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast)

if __name__ == "__main__":
    cang = Girl()
    cang.about("canglaoshi")
