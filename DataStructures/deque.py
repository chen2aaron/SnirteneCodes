class Deque(object):

    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    @property
    def remove_front(self):
        return self.items.pop()

    @property
    def remove_rear(self):
        return self.items.pop(0)

    @property
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)


if __name__ == '__main__':
    d = Deque()