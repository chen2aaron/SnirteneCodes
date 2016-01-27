import requests
from bs4 import BeautifulSoup
import time


url = 'http://www.v2ex.com'

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
              'Referer': 'http://www.v2ex.com/signin',
              'Host': 'www.v2ex.com',
              }

login_data = {'u': 'x@gmail.com',
              'p': 'xyz',
              'next': '/'
              }
time.sleep(3)

session = requests.session()
url_login = url + '/signin'
response = session.get(url_login, headers=my_headers)
soup = BeautifulSoup(response.content, "html.parser")

once = soup.find('input', attrs={'name': 'once'}).get('value').encode('utf-8')


login_data['once'] = once

login_s = session.post(url_login, login_data, headers=my_headers)

daily = url + '/mission/daily'

r = session.get(daily, headers=my_headers)
soupDaily = BeautifulSoup(r.text, "html.parser")

item = soupDaily.find('input', class_='super normal button').get('onclick')
mission_url = url + item.split("'")[1]

mission_r = session.get(mission_url, headers=my_headers)