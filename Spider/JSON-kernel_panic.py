#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-30
# Blog: morningchen.com

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
r = requests.get("http://www.lizhi.fm/api/radio_audios?s=0&l=20&band=474221")
content = r.text
result = json.loads(content)
for i in result:
    print i['url']
