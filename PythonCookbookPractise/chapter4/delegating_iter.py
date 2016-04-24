# 4.2. Delegating Iteration


class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    root.add_children(c1)
    root.add_children(c2)
    print(root)
    print(root._children)
    print(root.__iter__())
    for c in root:
        print(c)
