import re

f = open('ocr.txt', 'r')
str = f.read()
res = re.findall(r"[a-zA-Z]", str)
print ''.join(res)
import string
print ''.join([i for i in open('ocr.txt').read() if i in string.ascii_letters])
