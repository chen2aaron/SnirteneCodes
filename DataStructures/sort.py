import random
import os


def bubble_sort(data):
    """Time Complexity: O(n2)"""
    pass_num = len(data) - 1
    exchange = True
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if data[i] > data[i+1]:
                exchange = True
                data[i], data[i+1] = data[i+1], data[i]

        print(data)
        pass_num -= 1


def selection_sort(data):
    """Time Complexity: O(n2)"""
    for fill_sort in range(len(data)-1, 0, -1):
        max_position = 0
        for location in range(fill_sort + 1):
            if data[location] > data[max_position]:
                max_position = location
        data[max_position], data[fill_sort] = data[fill_sort], data[max_position]
        print(data)


def partition(seq):
    pi, seq = seq[0], seq[1:] # Pick and remove the pivot
    lo = [x for x in seq if x <= pi] # All the small elements
    hi = [x for x in seq if x > pi] # All the large ones
    return lo, pi, hi # pi is "in the right place"


def quick_sort(seq):
    if len(seq) <= 1:
        return seq # Base case
    lo, pi, hi = partition(seq) # pi is in its place
    return quick_sort(lo) + [pi] + quick_sort(hi) # Sort lo and hi separately

if __name__ == '__main__':
    data = [random.randint(1, 100) for i in range(10)]
    # data = [31, 13, 46, 69, 27, 23, 35, 82, 36, 64]
    print(data)
    # bubble_sort(data)
    selection_sort(data)



