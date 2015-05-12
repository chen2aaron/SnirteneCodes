#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-8
# Blog: morningchen.com
'''This is a game on http://www.pythonchallenge.com/pc/def/map.html'''

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def trans(lettter):
    if "a" <= lettter <= "x":
        trans = chr(ord(lettter) + 2)
        return trans
    elif lettter == "y":
        return "a"
    elif lettter == "z":
        return "b"
    else:
        return lettter


def duang(text):
    result = []
    text_list = text.split(" ")
    for word in text_list:
        word_list = list(word)
        translate_word = "".join(map(trans, word_list))
        result.append(translate_word)
    trans_text = " ".join(result)
    return trans_text

print duang(text)
print duang("map")


# 用推荐的方法maketrans  只用了一句，打击好大，我突然意识到我是不是造了个轮子
import string

transfun = string.maketrans(
    'abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print text.translate(transfun)
print 'map'.translate(transfun)
