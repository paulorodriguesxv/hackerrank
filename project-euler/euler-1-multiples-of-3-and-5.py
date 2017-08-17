#!/bin/python3

import sys

def discovery_max_div(number, m):
    max_number = number - 1
    while max_number % m != 0:
        max_number -= 1
    return max_number

def execute(number):
    total = 0

    if number > 3:
        max_div_3 = discovery_max_div(number, 3)
        total = ((max_div_3 // 3) * (3 + max_div_3)) // 2

    if number > 5:
        max_div_5 = discovery_max_div(number, 5)
        total += ((max_div_5 // 5) * (5 + max_div_5)) // 2

    if number > 15:
        max_div_15 = discovery_max_div(number, 15)
        total -= ((max_div_15 // 15) * (15 + max_div_15)) // 2

    return total


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(execute(n))