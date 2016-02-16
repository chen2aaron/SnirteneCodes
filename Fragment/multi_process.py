from multiprocessing import Process, Pool ,Queue
import os, time, random
import threading


def write(q):
    for v in ['A', 'B', 'C']:
        print('Put %s to queue...' % v)
        print('Write subprocess pid %s, parents %s' % (os.getpid(), os.getppid()))
        q.put(v)
        time.sleep(random.random())


def read(q):
    while True:
        v = q.get(True)
        print('Get %s from queue.' % v)
        print('Get subprocess pid %s, parents %s' % (os.getpid(), os.getppid()))


def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    """
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    """
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
