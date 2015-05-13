#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-13
# Blog: morningchen.com
"""
    函数式编程典型:filter, map, reduce
    pipeline:
    让每个功能就做一件事，并把这件事做到极致，
    软件或程序的拼装会变得更为简单和直观。
    这个设计理念影响非常深远，包括今天的Web Service，
    云计算，以及大数据的流式计算等等
"""


def even_filter(nums):
    return filter(lambda x: x % 2 == 0, nums)


def multiply_by_three(nums):
    return map(lambda x: x * 3, nums)


def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)


def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a),
                  fns,
                  data)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = pipeline_func(nums, [even_filter,
                              multiply_by_three,
                              convert_to_string])

print result
