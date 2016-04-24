# 4.6. Defining Generator Functions with Extra State
from collections import deque


class LineHistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('file.txt', encoding='utf-8') as f:
    lines = LineHistory(f)
    for line in lines:
        if 'Python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline))

    # output: 1, 12 ,123, 234
