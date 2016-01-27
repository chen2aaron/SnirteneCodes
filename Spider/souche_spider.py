# -*- coding:utf-8 -*-
import requests
import re
import json
from time import sleep
from Utils import torndb, sql


"""
brands_list_url 搜车网的获取汽车品牌接口
请求参数
    'type': 'car-subdivision',
返回json为
    {'items': [{'check': None,
                'code': 'brand-170',
                'dindex': 2147483647,
                'enName': '中兴',
                'extString': '{pinyin=zhongxing}',
                'id': None,
                'level': None,
                'name': 'Z 中兴',
                'parentCode': None,
                'type': None,
                'updateDate': None},

               ]
     }

brand_url 获取某汽车品牌下的各个系列
请求参数:
    'type': 'car-subdivision',
    'code': brand-code,
返回json为
    {
    'keys': ['阿尔法罗密欧'],
    'codes': {'阿尔法罗密欧': [{'check': None,
                           'code': 'series-671',
                           'dindex': 2147483647,
                           'enName': 'ALFA 156',
                           'extString': '{factory=阿尔法罗密欧, pinyin=ALFA 156}',
                           'id': None,
                           'level': None,
                           'name': 'ALFA 156',
                           'parentCode': None,
                           'type': None,
                           'updateDate': None},
                          {'check': None,
                           'code': 'series-672',
                           'dindex': 2147483647,
                           'enName': 'ALFA 166',
                           'extString': '{factory=阿尔法罗密欧, pinyin=ALFA 166}',
                           'id': None,
                           'level': None,
                           'name': 'ALFA 166',
                           'parentCode': None,
                           'type': None,
                           'updateDate': None},
                          {'check': None,
                           'code': 'series-1222',
                           'dindex': 2147483647,
                           'enName': 'ALFA GT',
                           'extString': '{factory=阿尔法罗密欧, pinyin=ALFA GT}',
                           'id': None,
                           'level': None,
                           'name': 'ALFA GT',
                           'parentCode': None,
                           'type': None,
                           'updateDate': None}]},
     }

series_url 获取某汽车某系列下的各个车辆型号
请求参数:
    'type': 'car-subdivision',
    'code': series-code,
返回json为
    {
    'items': [{'check': None,
               'code': '32632',
               'dindex': 2147483647,
               'enName': '2014款  Vanquish  6.0L 百年纪念版',
               'extString': '{}',
               'id': None,
               'level': None,
               'name': '2014款  Vanquish  6.0L 百年纪念版',
               'parentCode': None,
               'type': None,
               'updateDate': None},
              ]
    }
"""

brands_list_url = 'http://souche.com/pages/dicAction/loadRootLevel.json'
brand_url = 'http://souche.com/pages/dicAction/loadRootLevelForCar.json'
series_url = 'http://souche.com/pages/dicAction/loadNextLevel.json'


def db_client():
    db = torndb.Connection(
        host='127.0.0.1:3306',
        database='play',
        user='root',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
    )
    return db


def get_brands():
    """
    获取大搜车的汽车品牌code
    """
    brands_code = []
    with open('souche_brand.html', 'r') as f:
        for line in f.readlines():
            brand_code = re.findall(r'data-code=(\S+)', line)
            if brand_code:
                brands_code.append(brand_code[0])
    print(brands_code)
    print('total: %s' % len(brands_code))
    return brands_code


def get(url, code=None):
    """
    通用get请求
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Origin': 'http://souche.com',
        'Referer': 'http://souche.com/pages/caruser/sell_car.html',
        }
    params = {
        'type': 'car-subdivision',
        'code': code,
        }
    resp = requests.get(url, params=params, headers=headers)
    return json.dumps(resp.json())


def save_into_db(brand_code, data):
    args = {
        'brand_code': brand_code,
        'data': data,
    }
    db_client().execute(*sql.insert('car_json', args))
    print('------ brand_code: %s -------' % brand_code)
    sleep(2)


if __name__ == '__main__':
    rows = db_client().query('select * from car_series_url where data=%s', '')
    print(rows)
    for row in rows:
        series_code = row.series_code
        resp = get(series_url, series_code)
        db_client().update('update car_series_url set data=%s where series_code=%s', resp, series_code)
        print(row.series_code)

    # rows = db_client().query('select series_code from car_series order by id desc limit %s', 728)
    # count = 240
    # codes=[]
    # for row in rows:
    #     series_code = row.series_code
    #     codes.append(series_code)
    #     print('第 %s 次: %s' % (count, series_code))
    #     count += 1
    # codes.reverse()
    #
    # for c in codes:
    #     print(c)
    #     data = get(series_url, c)
    #     try:
    #         db_client().execute(*sql.insert('car_series_url', {'series_code':c, 'data': data}))
    #     except:
    #         db_client().execute(*sql.insert('car_series_url', {'series_code':c, 'data': ''}))
    #     sleep(0.6)

    # for i in data:
    #
    # print(data)

    # db_client().update('update car_json set brand_name=%s where brand_code=%s',)
    # print(json.loads(get(brands_list_url)))
