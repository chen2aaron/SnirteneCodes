# BlueBook code decryption
import sys


def sieve(n):
    x = [1] * n
    x[1] = 0
    for i in range(2, n / 2):
        j = 2 * i
        while j < n:
            x[j] = 0
            j = j + i
    return x
print sieve(100)
