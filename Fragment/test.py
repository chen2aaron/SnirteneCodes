#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-23
# Blog: morningchen.com
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('gb2312')
url = 'http://555ty.com/siwazhifu/index_1.html'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
req = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(req)
print response.read().decode('gb2312')
