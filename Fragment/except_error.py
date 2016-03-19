import logging

try:
    f = open('myfile.txt')
    s = f.readline()
except Exception as e:
    print(str(e))
    logging.warning('Failed:' + str(e))
