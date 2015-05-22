#!/usr/bin/env python
# -*- coding:utf-8 -*-
from os.path import join
class FileObject:
    '''对文件对象的包装，确保文件在关闭时得到删除'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # 按filepath，读写模式打开名为filename的文件
        self.file=open(join(filepath,filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file
