#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-26
# Blog: morningchen.com


import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

fp = open('result.txt', 'w')


def get_lizhifm_link(radio_id, mp3_numbers):
    """
        通过内部api
        得到http://www.lizhi.fm/#/35242的json文件
        http://www.lizhi.fm/api/radio_audios?band=35242&s=0&l=50
        band35242是IT工论频道 l意思是访问几个mp3文件
    """
    r = requests.get(
        "http://www.lizhi.fm/api/radio_audios?band=" + str(radio_id) + "&s=0&l=" + str(mp3_numbers))
    content = r.text
    result = json.loads(content)
    for i in result:
        print >>fp, i['url']

if __name__ == '__main__':
    get_lizhifm_link(35242, 100)
