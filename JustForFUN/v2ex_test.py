import requests, re

user = ''
pwd = ''

s = requests.Session()

headers = {
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://v2ex.com',
    'Referer': 'http://v2ex.com/signin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'
}

login_once = re.findall(r'value="(\d+)" name="once"', s.get('http://v2ex.com/signin').text)[0]
print(login_once)
data = {
    'u': user,
    'p': pwd,
    'once': login_once
}

# login
lo = s.post('http://v2ex.com/signin', data=data, headers=headers)
# print(lo.text)

# mission daily
daily_once = re.findall(r'once=(\d+)', s.get('http://v2ex.com/mission/daily').text)[0]
print(daily_once)
md = s.get('http://v2ex.com/mission/daily/redeem', data={'once': daily_once})