#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-30
# Blog: morningchen.com


import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

debug = True  # 设置是否打印log


def log(message):
    if debug:
        print message


def get_html(url):
    return requests.get(url).content


def download_stuff(url, save_path):
    try:
        with open(save_path, "wb") as temp:
            temp.write(get_html(url))
        log('Downloaded a image: ' + save_path)
    except Exception, e:
        print 'An error catched when download a image:', e


def download_images(url, save_path):
    soup = BeautifulSoup(get_html(url))
    for i in soup.find_all('div', {'class': 'panel panel-default'}):
        img_name = i.find('h3').text
        img_tag = i.find('img', {'class': "img-responsive"})
        img_link = img_tag.attrs['data-original']
        filename = '%s%s' % (img_name, img_link[-4:])
        download_stuff(img_link, save_path + filename)


def main():
    url = "http://www.bootstrapzero.com/bootstrap-templates"
    base_path = '/Users/chan/Pictures/Spider/bootstrapzero/'
    download_images(url, base_path)
if __name__ == '__main__':
    main()
