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
url = "http://music.163.com/api/dj/program/byradio?radioId=1364001&id=1364001&ids=%5B%221364001%22%5D&limit=10000&offset=0"
proxies = {
    "http": "http://127.0.0.1:8080",
}
headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://music.163.com/outchain/player?type=4&id=1364001&auto=1&height=430&bg=e8e8e8',
    'Cookie': 'NETEASE_WDA_UID=; __utma=; __utmz=; usertrack=xixijun; JSESSIONID-WYYY=92e72cea3d71e3e3866a0a32ad31fd50992d94e793ec6a16ae2bded447a541874a6962166441b8c43480074f944e4dad1c4e33c5b674e9ab22ec07180e52defe5e74aa22256169ac0fb9655b05869ecc04ea6565ea936657ff7218b457924992c458406207706c48c5bdaa74099dbb5ae49d200d8ef32dcb073721b449a6346e9f70f908; visited=true; __utma=94650624.1863944249.1432659609.1432659609.1432988561.2; __utmz=94650624.1432659609.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=94650624.11.10.1432988561; __utmc=94650624',
}
r = requests.get(url, headers=headers, proxies=proxies)
content = json.loads(r.text)
for i in content['programs']:
    print i['mainSong']['mp3Url']
