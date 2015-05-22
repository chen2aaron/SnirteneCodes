#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-23
# Blog: morningchen.com

import urllib2
import gzip
import StringIO
url = "http://"
response = urllib2.urlopen(url)
html = response.read()
html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode="r")
html = html.read().decode('latin-1').encode('utf-8')
print html
