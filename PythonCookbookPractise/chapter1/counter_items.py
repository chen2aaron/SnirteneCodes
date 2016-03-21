# 1.12. Determining the Most Frequently Occurring Items in a Sequence
from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(word_counts)
print(top_three)

more_words = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(more_words)
print(word_counts)

# 用途 制表或者计数数据的场合
a = Counter(word_counts)
b = Counter(more_words)
c = a + b
d = a - b
print(a)
print(b)
print(c)
print(d)