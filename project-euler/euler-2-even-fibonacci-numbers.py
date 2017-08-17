#!/bin/python3

import sys

def fibonacci(max):
    a, b = 1, 2
    while True:        
        if a >= max: break
        yield a
        a,b = b,a+b

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    f = fibonacci(n)
    total = 0
    for x in f:
        if x % 2 == 0:
            total += x

    print(total)    