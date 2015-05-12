#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-12
# Blog: morningchen.com


import json
from pprint import pprint

pprint(dir(json))
print json.__all__
data = {"name": "snirtene", "lang": (
    "python", "ruby", "object-c", "english"), "age": 24}
data_encoding = json.dumps(data)
print data_encoding
print "-" * 50
print type(data)
print type(data_encoding)

data_decoding = json.loads(data_encoding)
print data_decoding
print json.dumps(data, sort_keys=True, indent=2)
