# 2.4. Matching and Searching for Text Patterns
import re

text1 = '11/27/2012'
text2 = 'Nov 27 ,2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yep')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yep')
else:
    print('no')



date_pat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = date_pat.match('11/27/2012')
print(m)

print(m.group(0), m.group(1), m.groups(2), m.group(3), m.groups())
