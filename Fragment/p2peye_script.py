import requests
import json
from datetime import datetime
from pprint import pprint


def date_format(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


token_url = 'http://83.rmb.io/api/p2peye/token'
token_dict = {'username': 'cc', 'password': 'eve17068'}
token_ret = requests.get(token_url, params=token_dict).content.decode('utf-8')
token = json.loads(token_ret)['data']['token']
print('token params: ', token_dict)
print('token ret: ', token_ret)
print('token fetched: ', token)
print('\n', '* ' * 10, '\n')

# page_size = 20
# page_index = 1
# time_from = datetime(year=2015, month=1, day=1)
# time_to = datetime(year=2015, month=9, day=1)
# loans_url = 'http://83.rmb.io/api/p2peye/borrowings'
# loans_dict = {'token': token, 'page_size': page_size,
#               'page_index': page_index, 'time_from': date_format(time_from), 'time_to': date_format(time_to)}
# loans_ret = requests.get(loans_url, params=loans_dict).content.decode('utf-8')
# pprint(['loans params: ', loans_dict])
# pprint(['loans ret: ', json.loads(loans_ret)])
# print('\n', '* ' * 10, '\n')

page_size = 10
page_index = 1
time_from = datetime(year=2015, month=8, day=11)
time_to = datetime(year=2015, month=8, day=12)
loans_url = 'http://83.rmb.io/api/p2peye/investments'
loans_dict = {
    'token': token,
    'page_size': page_size,
    'id': 283      ,
    'page_index': page_index,
    'time_from': '',
    'time_to': '',
}
loans_ret = requests.get(loans_url, params=loans_dict).content.decode('utf-8')
pprint(['loans params: ', loans_dict])
pprint(['loans ret: ', json.loads(loans_ret)])