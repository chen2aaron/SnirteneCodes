# -*- coding:utf-8 -*-
import json
from pprint import pprint
import re
import string
from time import sleep
from Utils import torndb, sql
from souche_spider import db_client, get, series_url


def save_car_brands():
    data = db_client().get('select data from car_list').data
    brands_list = json.loads(data)['items']
    for brand_dict in brands_list:
        pinyin = re.findall(r'pinyin=([^}]*)', brand_dict['extString'])[0]
        args = {
            'name': brand_dict['name'],
            'en_name': brand_dict['enName'],
            'brand_code': brand_dict['code'],
            'dindex': brand_dict['dindex'],
            'pinyin': pinyin,
        }
        db_client().execute(*sql.insert('car_brands', args))
        print('save name: %s' % brand_dict['name'])


def save_car_series(rows):
    # rows = db_client().query('select brand_code, data from car_brand_url')
    success_count = 0
    error_count = 0
    for row in rows:
        brand_code = row.brand_code
        raw_dict = json.loads(row.data)
        brand_name_list = raw_dict['keys']
        print(brand_name_list)
        for brand_name in brand_name_list:
            series_list = raw_dict['codes'][brand_name]
            for s in series_list:
                pinyin = re.findall(r'pinyin=([^}]*)', s['extString'])[0]
                factory = re.findall(r'factory=([^,]*)', s['extString'])[0]
                args = {
                    'name': s['name'],
                    'en_name': s['enName'],
                    'series_code': s['code'],
                    'dindex': s['dindex'],
                    'brand_code': brand_code,
                    'pinyin': pinyin,
                    'factory': factory,
                    '*created_at': 'NOW()',
                }
                if not db_client().get('select 1 from car_series where series_code=%s', s['code']):
                    print(args)
                    try:
                        db_client().execute(*sql.insert('car_series', args))
                        success_count += 1
                    except:
                        error_count += 1
                        print('[Error:] %s ' % s['code'])
    print('success insert car_series rows: %s' % success_count)
    print('error insert car_series rows: %s' % error_count)


def save_car_models(rows):
    # rows = db_client().query('select series_code, data from car_series_url')
    success_count = 0
    error_count = 0
    for row in rows:
        series_code = row.series_code
        raw_dict = json.loads(row.data)
        model_list = raw_dict['items']
        print('--- series_code: %s ---' % series_code)
        for m in model_list:
            args = {
                'series_code': series_code,
                'code': m['code'],
                'name': m['name'],
                'en_name': m['enName'],
                'dindex': m['dindex'],
                '*created_at': 'NOW()',
            }
            if not db_client().get('select 1 from car_models where code=%s', m['code']):
                print(args)
                try:
                    db_client().execute(*sql.insert('car_models', args))
                    success_count += 1
                except:
                    error_count += 1
                    print('[Error:] %s ' % m['code'])
    print('[success] insert car_models rows: %s' % success_count)
    print('[error] insert car_models rows: %s' % error_count)


def compare_series():
    """爬过之后对比不存在的数据整理到新表"""
    comparison = db_client().query('select cs.series_code, cs.en_name, cs.brand_code, cs.factory, csu.data '
                              'from car_series cs left join car_series_url csu on cs.series_code=csu.series_code '
                              'where data is null')
    for c in comparison:
        data = get(series_url, c.series_code)
        args = {
            'series_code': c.series_code,
            'data': data,
            '*spider_at': 'NOW()'
        }
        db_client().execute(*sql.insert('car_series_url', args))
        print(c.series_code)


def for_anti_spider():
    """再爬一次没爬到的数据"""
    rows = db_client().query('select series_code, data from car_series_url where length(data)=13 order by data')
    for row in rows:
        data = get(series_url, row.series_code)
        args = {
            'series_code': row.series_code,
            'data': data,
            '*spider_at': 'NOW()'
        }
        print(args)
        db_client().execute(*sql.update('car_series_url', args, {'series_code': row.series_code}))
    sleep(2)

def test1():
    rows = db_client().query('select brand_code, en_name, pinyin from car_brands order by pinyin')
    items = []
    for row in rows:
        brands = []
        dict(row.pinyin[0].upper()=brands)
        brands.append({
            'brand_code': row.brand_code,
            'en_name': row.en_name,
            'pinyin': row.pinyin, })
    if args:
        items.append(args)
    pprint(items)

def test2():

    brand_code = 'brand-15'
    if brand_code:
        factories = db_client().query('select distinct factory from car_series where brand_code=%s', brand_code)
        items = []
        for f in factories:
            rows = db_client().query('select series_code, en_name, pinyin, factory '
                                       'from car_series where brand_code=%s and factory=%s order by factory, pinyin', brand_code, f.factory)
            series = []
            for row in rows:
                series.append({
                    'en_name': row.en_name,
                    'series_code': row.series_code,
                    'pinyin': row.pinyin,
                })
            args = {
                'factory': f.factory,
                'series': series,
                }
            items.append(args)
        pprint(items)


def test3():

    series_code = 'series-5009-ly'
    if series_code:
        years = db_client().query('select distinct production_year from car_models where series_code=%s', series_code)
        items = []
        for y in years:
            rows = db_client().query('select en_name, code from car_models '
                                 'where series_code=%s and production_year=%s '
                                 'order by en_name desc', series_code, y.production_year)
            models = []
            for row in rows:
                models.append({
                    'en_name': row.en_name,
                    'code': row.code,
                    })
            args = {
                'year': y.production_year,
                'models': models,
                }
            items.append(args)
        pprint(items)

if __name__ == '__main__':
    # compare_series()
    # rows = db_client().query('select * from car_series_url where spider_at>%s', '2015-11-20 16:43:00')
    # save_car_models(rows)
    test1()
