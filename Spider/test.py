# coding: u8
import urllib2
import gzip
import StringIO
url = "http://555ty.com/siwazhifu/3352.html"
response = urllib2.urlopen(url)
html = response.read()
html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode="r")
html = html.read().decode('latin-1').encode('utf-8')
print html
