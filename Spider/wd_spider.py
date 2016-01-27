from __future__ import print_function

import json
import random
import string
import sys
import sqlite3

import time
import requests
import requests.packages

requests.packages.urllib3.disable_warnings()


def main(range_str, fname):
    min_id, max_id = map(int, range_str.split('-'))
    conn = sqlite3.connect(fname)
    cursor = conn.cursor()
    cursor.execute('create table if not exists wd(id INTEGER PRIMARY KEY, content TEXT)')
    cursor.execute('select max(id) from wd')
    db_min_id = cursor.fetchone()[0] or 1

    min_id = max(min_id, db_min_id+1)

    for bid in range(min_id, max_id+1):
        fetch(bid, cursor)
        conn.commit()


def fetch(bid, cursor):
    page = 1
    page_size = 30
    url = 'https://www.weidai.com.cn/bid/tenderListPage?page=%s&rows=%s&bid=%s'

    headers = {
        'Referer': 'https://www.weidai.com.cn/bid/showBorrowDetail?bid=%s&timing=0&productTypeId=1' % bid,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/437.36 (KHTML, like Gecko) Chrome/43.0.2708.222 Safari/267.92',
        'X-Requested-With': 'XMLHttpRequest',
    }
    cookies = {
        'JSESSIONID': ''.join(random.sample(string.ascii_uppercase + string.digits, 32)),
        'SERVERID': '%s|%s|%s' % (''.join(random.sample(string.ascii_lowercase + string.digits, 32)), time.time(), time.time()),
    }
    proxy = {
        'http': 'http://5ac4d9eaeb6c4cd0ac1015ec76a1566f:@proxy.crawlera.com:8010',
        'https': 'http://5ac4d9eaeb6c4cd0ac1015ec76a1566f:@proxy.crawlera.com:8010',
    }
    while True:
        try:
            resp = requests.get(url % (page, page_size, bid), verify=False, headers=headers, cookies=cookies)
        except Exception as e:
            print(bid, page, page_size, 'error', e)
            return

        cursor.execute('insert into wd(id, content) values (?, ?)', (bid, resp.text))
        print(bid, page, page_size, 'success')

        resp = json.loads(resp.text, encoding='utf-8')
        if resp['total'] < page_size:
            return

        page += 1

if __name__ == '__main__':
    args = sys.argv[1:3]
    main(*sys.argv[1:3])