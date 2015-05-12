# coding: utf8
'''
问题描述

如果将一句话作为一个字符串，那么这个字符串中必然会有
空格（这里仅讨论英文），比如"How are you."，但有的
时候，会在两个单词之间多大一个空格。现在的任务是，如
果一个字符串中有连续的两个空格，请把它删除。


by AaronChen
'''
string = "I love  code."
print string

str_list = string.split(" ")
print str_list
word = [s.strip() for s in str_list if s != ""]
print word

print " ".join(word)
