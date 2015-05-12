#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-12
# Blog: morningchen.com


import requests
payload = {"key1": "value1", "key2": "value2"}
r = requests.post("http://httpbin.org/post")
r1 = requests.post("http://httpbin.org/post", data=payload)
