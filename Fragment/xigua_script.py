import requests
import json
host = 'http://api.83chedai.com'


borrowings_url = host + '/api/xigualicai/borrowings'
resp = requests.get(borrowings_url)
borrowings = resp.json()
print('recordCount: %s' % borrowings['recordCount'])
print('transferTime: %s' % borrowings['transferTime'])

# borrowing_url = host + '/api/xigualicai/borrowing'
# borrowing_list = ','.join([str(i) for i in range(1000,2101)])
# params = {'queryProductIdList': borrowing_list}
# borrowing_resp = requests.get(borrowing_url, params=params)
# borrowing = borrowing_resp.json()

# series_url = host + '/api/xigualicai/series'
# series_resp = requests.get(series_url)
# series = series_resp.json()
