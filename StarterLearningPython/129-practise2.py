# coding: utf8
'''
问题描述

按照下面的要求实现对列表的操作：

1.产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
2.如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
3.对上面的列表元素从大到小排序

by AaronChen
'''
import random
name = range(40)
score = {}
n = 0
for i in name:
    score[i] = random.randint(0, 100)
print score

avg = float(sum(score.values())) / len(score)
print "The average score is %.1f" % avg
for i in name:
    if score[i] < avg:
        n = n + 1
print "There are %d students less than average." % n

print sorted(score.values(), reverse=True)
