# 2.2. Matching Text at the Start or End of a String
import os
import re


files = os.listdir('.')
# 用tuple 匹配多种可能
filter_file = [f for f in files if f.endswith(('.py', '.pyc'))]

urls = [
    'http://www.python.org',
    'https://google.com',
    'as://dasd.co',
    'ftp://sadasda.co',
]
filter_url = [url for url in urls if re.match(r'http:|https:|ftp:', url)]
print(filter_url)
