#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-12
# Blog: morningchen.com


import requests
from pprint import pprint
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# pprint(dir(requests))
# print requests.__doc__

r = requests.get("http://morningchen.com")
# pprint(r.cookies)
print r.headers
print r.encoding
# print r.text
print r.content
