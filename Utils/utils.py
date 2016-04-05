# -*- coding: utf-8 -*-
import base64
import hmac
import string
from hashlib import sha1
from Crypto.Cipher import AES
import time
from datetime import datetime, date, timedelta
from decimal import Decimal
import hashlib
import json
import random
import re


class PropDict(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        return self[name] if name in self else None


class EmptyDict(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        return self[name] if name in self else ''


def json_default(dt_fmt='%Y-%m-%d %H:%M:%S', date_fmt='%Y-%m-%d', decimal_fmt=str):
    def _default(obj):
        if isinstance(obj, datetime):
            return obj.strftime(dt_fmt)
        elif isinstance(obj, date):
            return obj.strftime(date_fmt)
        elif isinstance(obj, Decimal):
            return decimal_fmt(obj)
        else:
            raise TypeError('%r is not JSON serializable' % obj)
    return _default


def json_dumps(obj, dt_fmt='%Y-%m-%d %H:%M:%S', date_fmt='%Y-%m-%d', decimal_fmt=str, ensure_ascii=False):
    return json.dumps(obj, ensure_ascii=ensure_ascii, default=json_default(dt_fmt, date_fmt, decimal_fmt))


def json_hook(pairs):
        """ convert json object to python object """
        return JsonDict(pairs)


class JsonDict(dict):
    """ general json object that allows attributes to be bound to and also behaves like a dict """

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


def generate_duration(start_arg, end_arg):
    """根据参数确定时间轴范围"""
    # 没指定日期，默认显示7天
    if not (start_arg and end_arg):
        today = date.today()
        start = today - timedelta(days=6)
        end = today - timedelta(days=0)
        duration = (end - start).days + 1
    else:
        start = datetime.strptime(start_arg, '%Y-%m-%d').date()
        end = datetime.strptime(end_arg, '%Y-%m-%d').date()
        duration = (end - start).days + 1
    # 根据时间间隔获得时间轴
    categories = [(start + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(duration)]

    return categories, start, end


def sql_in(ls):
    return ','.join(['%s']*len(ls))


def sql_in_dict(d):
    return ','.join(['%s=%%s' % field for field in d])


des_padding = lambda s: s + (8 - len(s) % 8) * chr(8 - len(s) % 8)
aes_padding = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
des_unpadding = aes_unpadding = lambda s: s[0:-s[-1]]


def aes_encrypt(content, secret_key):
    return base64.b64encode(AES.new(secret_key).encrypt(aes_padding(content)))


def aes_decrypt(content, secret_key):
    return aes_unpadding(AES.new(secret_key).decrypt(base64.b64decode(content)))


def md5_encrypt(content):
    return hashlib.md5(content.encode()).hexdigest()


def sms_code():
    return '{:0>6}'.format(random.randint(0, 999999))


def gen_ticket():
    return ''.join(random.sample(string.ascii_letters + string.digits, 12))


def order_no_tail():
    return ''.join(random.sample(string.ascii_letters + string.digits, 4))


def hide(s, front, hide_num=0, back=0):
    """15655447788 -> 156******88"""
    if hide_num < 0 or back < 0:
        if front+hide_num+back != len(s):
            return False
    id_tmp = s if isinstance(s, list) else list(s)
    if hide_num or back:
        if front < 0:
            return False
        if back:
            id_tmp[front:-back] = '*' * (len(id_tmp)-front-back)
            return ''.join(id_tmp)
        id_tmp[front:front+hide_num] = '*' * (hide_num if front+hide_num <= len(s) else len(s)-front)
        return ''.join(id_tmp)
    else:
        id_tmp[front:] = '*' * (abs(front) if front < 0 else len(s)-front)
        return ''.join(id_tmp)


def mask(s, start=0, end=None, fill_with='*'):
    """ 将指定范围内的字符替换成指定字符，范围规则与 list 切片一致 """
    sl = list(s)
    if end is None:
        end = len(sl)
    sl[start:end] = fill_with*len(sl[start:end])
    return ''.join(sl)


def qf(money, only_int=False):
    """ 金额的千分表示 """
    return '{0:,}'.format(round(money, 0) if only_int else money)


ic_factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
ic_re = re.compile(r'(^\d{15}$)|(^\d{17}([0-9]|x|X)$)')


def is_ic(sn):
    if not ic_re.match(sn):
        return False
    if len(sn) == 18 and sn[-1].upper() != '10X98765432'[sum(int(a)*b for a, b in zip(sn[:17], ic_factor)) % 11]:
        return False
    return True


def uno():
    return int(time.time()*1000000)


def int2ip(int_ip):
    """ip to int"""
    return '.'.join([str(int_ip//(256**i) % 256) for i in range(3, -1, -1)])


def ip2int(ip):
    """int to ip"""
    return sum([256**j*int(i) for j, i in enumerate(ip.split('.')[::-1])])


def dt_truncate(dt):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def dt_ceiling(dt):
    return dt.replace(hour=23, minute=59, second=59, microsecond=0)


def generate_private_uri(key, personal='', style='', prefix=None, rotate=None):
    if not personal:
        key = 'uploads/' + key

    if prefix is None:
        prefix = options.private_img_uri

    expires = str(int(time.time()) + 300)
    h = hmac.new(options.aliyun_secret.encode('utf-8'),
                 ('GET\n\n\n' + expires + '\n/' + options.oss_bucket_private + '/' + key + style).encode('utf-8'), sha1)
    sign = base64.encodebytes(h.digest()).strip()
    params = {
        'OSSAccessKeyId': options.aliyun_access_key,
        'Expires': expires,
        'Signature': sign,
    }
    url = prefix + '/' + key + style # + '?' + urllib.parse.urlencode(params)
    if rotate:
        url += ('_' if style else '@') + str(rotate) + 'r'
    return url


def bytes_to_str(s, ec='utf-8'):
    return s if isinstance(s, str) else s.decode(ec)
