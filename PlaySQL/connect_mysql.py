# -*- coding:utf8 -*-
# Author: xixijun
# Github: github.com/chen2aaron
# Date: 15/7/17
# Python 3.4
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='123456',
    db='play',
    port=3306,
    charset='utf8')

