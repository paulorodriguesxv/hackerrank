#!/bin/python3

import sys

def get_palindrome(limit):
    max_palindrome = 101101
    for i in range(999, 100, -1):
        for j in range(999, i-1, -1):
            prod = i * j
            
            if prod >= limit: continue
            if prod < max_palindrome: break
            
            if (str(prod) == str(prod)[::-1]):
                max_palindrome = prod                    
            
            j -= 1
        i -= 1

    return max_palindrome

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_palindrome(n))