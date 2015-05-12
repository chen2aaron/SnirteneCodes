#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Blog: morningchen.com
# Date: 15-5-7
'''
统计考试成绩
'''


def average_score(scores):
    '''
    平均分
    '''
    score_values = scores.values()
    sum_score = float(sum(score_values))
    average_score = sum_score / len(score_values)
    return average_score


def sorted_score(scores):
    '''
    成绩从高到低排序
    '''
    score_lst = [(scores[k], k) for k in scores]
    sort_lst = sorted(score_lst, reverse=True)
    return [(i[1], i[0]) for i in sort_lst]


def score_max(scores):
    '''
    分数最高的人
    '''
    lst = sorted_score(scores)
    score_max = lst[0][1]
    return [(i[0], i[1]) for i in lst if i[1] == score_max]


def score_min(scores):
    '''
    分数最低的人
    '''
    lst = sorted_score(scores)
    score_min = lst[len(lst) - 1][1]
    return [(i[0], i[1]) for i in lst if i[1] == score_min]

if __name__ == '__main__':
    n1_scores = {"zhangsan": 90, "lzw": 90,
                 "gnj": 90, "lisi": 78,
                 "wangermazi": 39}

    ave = average_score(n1_scores)
    print "平均分是 %.2f。" % ave
    paixu = sorted_score(n1_scores)
    print "分数从高到低排列：", paixu
    xueba = score_max(n1_scores)
    print "有请学霸登场：", xueba
    xuezha = score_min(n1_scores)
    print "学渣们不要再撸了：", xuezha
