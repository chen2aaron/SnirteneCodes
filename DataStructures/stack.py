class Stack(object):
    """LIFO 后进先出"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    @property
    def pop(self):
        return self.items.pop()

    @property
    def peek(self):
        return self.items[len(self.items) - 1]

    @property
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)


if __name__ == '__main__':
    s = Stack()
