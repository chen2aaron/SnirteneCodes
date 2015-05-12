#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-12
# Blog: morningchen.com


import tempfile  # 临时文件模块
import json
data = {"name": "snirtene", "lang": (
    "python", "ruby", "object-c", "english"), "age": 24}

print tempfile.__all__
# 临时文件 w+ 消除文件内容，然后以读写方式打开文件。
f = tempfile.NamedTemporaryFile(mode="w+")
json.dump(data, f)
f.flush()
print open(f.name, "r").read()

