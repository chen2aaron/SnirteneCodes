# coding: utf8

f = open("/Users/chan/Desktop/心路历程.md", "r")
while True:
    line = f.readline()
    if not line:
        break
    print line,
f.close()
