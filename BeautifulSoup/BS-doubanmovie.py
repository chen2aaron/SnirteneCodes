#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-22
# Blog: morningchen.com
import sys
import urllib
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


def get_url(url):
    """
        得到url的HTML文本
    """
    return urllib.urlopen(url).read()


def find_em_title(url):
    """
        打印当前url显示的豆瓣电影排名
    """
    soup = BeautifulSoup(get_url(url))
    for hd_div in soup.find_all('div', class_='item'):
        title = hd_div.span.get_text() # 筛选出标题
        em = hd_div.em.get_text() # 筛选出排名
        print em.rjust(2) + "  " + title


def all_url(count_page=0):
    """
        豆瓣电影前250名，每页显示25名，共10页
    """
    page = 25*count_page
    url = "http://movie.douban.com/top250?start=%s&filter=&type=" % page
    return url


def main():
    """
        循环调用10页
    """
    for i in xrange(10):
        find_em_title(all_url(i))


if __name__ == '__main__':
    main()
