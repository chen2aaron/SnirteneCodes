import sched
import time
from datetime import datetime


def func(msg):
    print "call func time:", datetime.now(), "msg:", msg

if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)
    print "--start %s --" % datetime.now()
    s.enter(1, 2, func, ('small event',))
    s.enter(3, 3, func, ('big event',))
    s.run()
    print "--end %s --" % datetime.now()
