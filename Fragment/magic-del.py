#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-14
# Blog: morningchen.com

from os import getcwd
from os.path import join


class FileObject:

    '''给文件对象进行包装从而确认在删除时文件流关闭'''

    def __init__(self, filepath=getcwd(), filename='sample.txt'):
        # 读写模式打开一个文件
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file

# x = FileObject
