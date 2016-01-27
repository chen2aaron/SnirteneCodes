import threading
from datetime import datetime


def test_func(msg1, msg2):
    print "call test_func at,",datetime.now(), msg1, msg2

if __name__ == '__main__':
    print "--start %s --" % datetime.now()
    t = threading.Timer(5, test_func, ('good', 'morning'))
    t.start()
    print "--end %s --" % datetime.now()
