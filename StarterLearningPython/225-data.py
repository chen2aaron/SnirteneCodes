#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-11
# Blog: morningchen.com
import urllib
import urllib2

url = 'http://www.itdiffer.com/register.py'

values = {'name': 'qiwsir',
          'location': 'China',
          'language': 'Python'}

data = urllib.urlencode(values)     # 编码
req = urllib2.Request(url, data)    # 发送请求同时传data表单
# response = urllib2.urlopen(req)  # 接受反馈的信息
# the_page = response.read()  # 读取反馈的内容
print data
print req
