
from Utils import torndb, sql
import json

def db():
    db = torndb.Connection(
        host='127.0.0.1:3366',
        database='',
        user='',
        password='',
        time_zone='+8:00',
        charset='utf8mb4',
        read_timeout=10,
        write_timeout=15,
    )
    return db


bank_limits_data = {
    'COMM':   {'name': '交通银行', 'quick': 20000, 'binding_first': 20000, 'binding': 50000, 'one_day': 500000},
    'BOC':    {'name': '中国银行', 'quick': 10000, 'binding_first': 10000, 'binding': 10000, 'one_day': 10000},
    'ABC':    {'name': '农业银行', 'quick': 5000,  'binding_first': 20000, 'binding': 20000, 'one_day': 100000},
    'CCB':    {'name': '建设银行', 'quick': 50000, 'binding_first': 50000, 'binding': 50000, 'one_day': 500000},
    'ICBC':   {'name': '工商银行', 'quick': 50000, 'binding_first': 50000, 'binding': 50000, 'one_day': 50000},
    'CITIC':  {'name': '中信银行', 'quick': 50000, 'binding_first': 50000, 'binding': 50000, 'one_day': 500000},
    'CMBC':   {'name': '民生银行', 'quick': 5000,  'binding_first': 50000, 'binding': 50000, 'one_day': 1000000},
    'CIB':    {'name': '兴业银行', 'quick': 50000, 'binding_first': 50000, 'binding': 50000, 'one_day': 50000},
    'CEB':    {'name': '光大银行', 'quick': 50000, 'binding_first': 50000, 'binding': 50000, 'one_day': 500000},
    'BOS':    {'name': '上海银行', 'quick': 5000,  'binding_first': 5000,  'binding': 5000,  'one_day': 50000},
    'PSBC':   {'name': '邮储银行', 'quick': 0,     'binding_first': 5000,  'binding': 5000,  'one_day': 5000},
    'SZPAB':  {'name': '平安银行', 'quick': 5000,  'binding_first': 5000,  'binding': 5000,  'one_day': 5000},
    'SPDB':   {'name': '浦发银行', 'quick': 5000,  'binding_first': 20000, 'binding': 20000,  'one_day': 50000},
    'CMB':    {'name': '招商银行', 'quick': 5000,  'binding_first': 50000, 'binding': 50000, 'one_day': 300000},
    'HXB':    {'name': '华夏银行', 'quick': 5000,  'binding_first': 5000,  'binding': 5000,  'one_day': 50000},
    'GDB':    {'name': '广发银行', 'quick': 5000,  'binding_first': 5000,  'binding': 50000, 'one_day': 1000000}
}

for k, v in bank_limits_data.items():
    try:
        db().update('update banks set quick_limit=%s, binding_first_limit=%s, binding_limit=%s, one_day_limit=%s '
                    'where code=%s', v['quick'], v['binding_first'], v['binding'], v['one_day'], k)
    except Exception as e:
        print(k)
        print(e)
