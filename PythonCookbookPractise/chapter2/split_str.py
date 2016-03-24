# 2.1. Splitting Strings on Any of Multiple Delimiters
import re

line = 'asdf fjdk; afed, fjek,asdf, foo, alskdj'
s = re.split(r'[;,\s]\s*', line)
print(s)
# 保留分割字符
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
