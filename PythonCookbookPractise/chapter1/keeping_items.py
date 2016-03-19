# 1.3. Keeping the Last N Items
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for l in lines:
        if pattern in l:
            yield l, previous_lines
        previous_lines.append(l)


if __name__ == '__main__':
    with open(r'./file', 'r', encoding='utf-8') as f:
        for line, prevlines in search(f, 'Python'):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
