#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-23
# Blog: morningchen.com
import sys
import requests
import StringIO
from bs4 import BeautifulSoup
from gzip import GzipFile
reload(sys)
sys.setdefaultencoding('utf-8')


def get_url(url):
    """
        得到url的HTML文本
    """
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) '
    headers = {'User-Agent': user_agent}
    req = requests.request('GET', url)
    return req.text


url = "http://555ty.com/siwazhifu/3352.html"
# print get_url(url)
r = requests.get(url)
html_data = GzipFile(fileobj=StringIO(r), mode="r").read()
# print get_url(url)
print html_data
