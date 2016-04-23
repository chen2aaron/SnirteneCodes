# -*- coding: utf-8 -*-
import re

USE_SOCKS_PROXY = 0

if USE_SOCKS_PROXY:
    import requesocks as requests
else:
    import requests
# import socks, socket
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
# socket.socket = socks.socksocket
username = 'x@gmail.com'
password = 'xyz'

host = 'http://www.v2ex.com'
signin_url = host + '/signin'
mission_url = host + '/mission/daily'
coin_url = mission_url + '/redeem'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Origin': 'http://v2ex.com',
    'Referer': 'http://v2ex.com/signin',
}

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080'
}

params = {
    'u': username,
    'p': password,
    'next': '/',
}

# 建立session
s = requests.session()
# s.proxies = proxies if USE_SOCKS_PROXY else ''

# 请求登陆页面 获取once值
signin_resp = s.get(signin_url)
signin_once = re.findall(r'value="(\d+)" name="once"', signin_resp.text)[0]

# 将once加入POST表单中 请求登陆
params['once'] = signin_once
r = s.post(url=signin_url, data=params, headers=headers, verify=True)
if r.url != host + '/':
    print('FAIL: %s' % r.url)
else:
    # 登陆成功 请求/mission/daily页面 获取once值
    daily_once = re.findall(r'once=(\d+)', s.get(mission_url).text)[0]
    if daily_once:
        # 拿到once请求/mission/daily/redeem
        resp = s.get(url=coin_url, data={'once': daily_once}, headers=headers, verify=True)
        print('SUCCESS: %s' % resp.url)
    else:
        print('BOOM: %s' % daily_once)

