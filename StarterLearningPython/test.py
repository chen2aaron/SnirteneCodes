#-*- coding:utf-8 -*-

import urllib2
import json
import re

SearchIphoneUrl = 'http://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&enc=utf-8&qr=&qrst=UNEXPAND&as_key=title_key%2C%2C%E6%89%8B%E6%9C%BA&rt=1&stop=1&click=&psort=1&page=1'
header = {'User-Agent':
          'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0', 'Accept': '*/*'}


def getHtmlSrc(url, header):
    req = urllib2.Request(url, header)
    res = urllib2.urlopen(url, timeout=5)
    htmlSrc = res.read()
    return htmlSrc


def saveHtmlSrc(url):
    html = getHtmlSrc(url, header)
    with open('jd_iphone.txt', 'w') as f:
        f.write(html)

saveHtmlSrc(SearchIphoneUrl)
print '++++++++++++++++++++京东放养的爬虫++++++++++++++++++++'

with open('jd_iphone.txt', 'r') as fhtml:
    localhtml = fhtml.read()
    # .replace("'",'"').replace(' ','')
    for skuid in re.findall('', localhtml):
        # 商品编号
        sku = skuid.split('"')[1]
        # 手机名称
        pname = re.search('''苹果(.*?)手机(.*?)''' % sku, localhtml)
        # 正则取商品名称
        html
        # 手机价格
        price = re.search('''''' % sku, localhtml)
        if(pname != '' and price != ''):
            print "商品编号：%s" % sku
            print "名称：%s\n价格：%s\n\n" % (pname.group(1), price.group(1))
            print '++++++++++++++++++++京东放养的爬虫++++++++++++++++++++'
