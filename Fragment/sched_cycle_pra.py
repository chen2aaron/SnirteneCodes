import sched
import time
from datetime import datetime


s = sched.scheduler(time.time, time.sleep)


def func(action_at):
    print "call func time:", datetime.now(), action_at
    s.enterabs(action_at + 5, 1, func, (action_at + 5,))


if __name__ == "__main__":
    print "--start %s --" % datetime.now()
    init_time = time.time()
    s.enterabs(init_time, 1, func, (init_time,))
    s.run()
    print "--end %s --" % datetime.now()
