#!/bin/python

import sys


def get_largest_prime(number):
    d = 2

    while (number > 1):
        while (number % d == 0):
            yield d
            number //= d
        
        d += 1
        if (d*d > number):
            if (number > 1):
                yield number
            break


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max(get_largest_prime(n)))