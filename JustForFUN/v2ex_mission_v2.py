# -*- coding: utf-8 -*-
import re
import logging

import requests

logger = logging.getLogger('v2ex_log')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

formatter = logging.Formatter('[%(levelname)s %(lineno)d %(asctime)s] %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


def v2ex_mission():
    host = 'http://www.v2ex.com/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0',
        'Origin': 'http://v2ex.com',
        'Referer': 'http://v2ex.com/signin',
    }

    s = requests.session()

    signin_resp = s.get(host + 'signin')
    if signin_resp.status_code != 200:
        return logger.error('get signin failed')
    logger.info('get signin success')

    signin_once = re.findall(r'value="(\d+)" name="once"', signin_resp.text)[0]
    username_filed = re.findall(r'<input type="text" class="sl" name="(\w+)"', signin_resp.text)[0]
    password_filed = re.findall(r'<input type="password" class="sl" name="(\w+)"', signin_resp.text)[0]

    params = {
        username_filed: 'username',
        password_filed: 'pwd',
        'next': '/',
        'once': signin_once,
    }

    r = s.post(url=host + 'signin', data=params, headers=headers, verify=True)

    if r.url != host:
        return logger.error('post signin failed')

    logger.info('post signin success')
    # 登陆成功 请求/mission/daily页面 获取once值
    daily_once = re.findall(r'once=(\d+)', s.get(host + 'mission/daily').text)[0]
    if not daily_once:
        return logger.error('could not find daily_once >.<')

    # 拿到once请求/mission/daily/redeem
    resp = s.get(url=host + 'mission/daily/redeem', data={'once': daily_once}, headers=headers, verify=True)
    if resp.status_code != 200:
        return logger.error('Fuck!')

    logger.info('Yep!, I got it!')


if __name__ == '__main__':
    v2ex_mission()
