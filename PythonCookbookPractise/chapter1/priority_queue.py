# 1.5. Implementing a Priority Queue
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __repr__(self):
        return str(self._queue)


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('python'), 6)
    q.push(Item('ruby'), 4)
    q.push(Item('r'), 3)
    q.push(Item('go'), 2)
    q.push(Item('java'), 9)
