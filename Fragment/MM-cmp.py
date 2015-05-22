#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Word(str):
    """
        继承str，单词类，比较定义是基于单词长度的
    """
    def __new__(cls, word):
        # 注意，我们使用了__new__,这是因为str是一个不可变类型，
        # 所以我们必须更早地初始化它（在创建时）
        if ' ' in word:
            print "单词内含有空格，截断到第一部分"
            word = word[:word.index(' ')] # 在出现第一个空格之前全是字符了现在
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

if __name__ == '__main__':
    a = Word('Magic Methods')
    b = Word('Maaaaa')
    print a.__gt__(b)
    print a.__lt__(b)
