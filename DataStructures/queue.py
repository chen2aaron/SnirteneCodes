class _Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue(object):
    """FIFO 先进先出"""
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def enqueue(self, item):
        n = self._last
        self._last = _Node(item)
        if self.is_empty:
            self._first = self._last
        else:
            n.next = self._last
        self._size += 1

    @property
    def dequeue(self):
        if self.is_empty:
            raise IndexError('dequeue from empty queue')
        n = self._first
        self._first = self._first.next
        self._size -= 1
        return n.item

    def peek(self):
        if self.is_empty:
            raise IndexError('peek at empty queue')
        return self._first.item

    def __iter__(self):
        current = self._first
        while current:
            yield current.item
            current = current.next

    def __str__(self):
        return ' '.join([str(i) for i in self])

    def __repr__(self):
        return "Queue(" + str(self) + ")"


if __name__ == '__main__':
    q = Queue()
