#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-23
# Blog: morningchen.com
import sys
import requests
import urllib
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


debug = True  # 设置是否打印log


def log(message):
    if debug:
        print message


def download_image(url, save_path):
    """
        根据图片url下载图片到save_path
    """
    try:
        urllib.urlretrieve(url, save_path)
        log('Downloaded a image: ' + save_path)
    except Exception, e:
        print 'An error catched when download a image:', e


def load_html(url):
    """
        得到url的HTML文本，解码
        关于乱码问题试了好多方法终于成功了
    """
    req = requests.request('GET', url)
    return req.text.encode('latin-1').decode('gb2312')


def down_images(url, save_dir):
    soup = BeautifulSoup(load_html(url))
    for li_tag in soup.find_all('li'):
        img_tag = li_tag.find('img')
        if img_tag is not None and img_tag.has_attr('alt' and 'src'):
            alt = img_tag.attrs['alt']  # 图片的介绍
            src = img_tag.attrs['src']  # 图片的地址
            filename = '%s%s' % (alt, src[-4:])
            download_image(src, save_dir + filename)


def main():
    url = "http://555ty.com/siwazhifu/index_1.html"
    base_path = '/Users/chan/Pictures/Spider/siwazhifu/'
    down_images(url, base_path)
if __name__ == '__main__':
    main()
