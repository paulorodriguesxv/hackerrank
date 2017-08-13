#!/bin/python

import operator

from itertools import count

from math import sqrt, ceil

def sieve_wheel_30(N):
    # http://zerovolt.com/?p=88
    ''' Returns a list of primes <= N using wheel criterion 2*3*5 = 30

Copyright 2009 by zerovolt.com
This code is free for non-commercial purposes, in which case you can just leave this comment as a credit for my work.
If you need this code for commercial purposes, please contact me by sending an email to: info [at] zerovolt [dot] com.'''
    __smallp = ( 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
    61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
    149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
    313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
    409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
    691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)

    wheel = (2, 3, 5)
    const = 30
    if N < 2:
        return []
    if N <= const:
        pos = 0
        while __smallp[pos] <= N:
            pos += 1
        return list(__smallp[:pos])
    # make the offsets list
    offsets = (7, 11, 13, 17, 19, 23, 29, 1)
    # prepare the list
    p = [2, 3, 5]
    dim = 2 + N // const
    tk1  = [True] * dim
    tk7  = [True] * dim
    tk11 = [True] * dim
    tk13 = [True] * dim
    tk17 = [True] * dim
    tk19 = [True] * dim
    tk23 = [True] * dim
    tk29 = [True] * dim
    tk1[0] = False
    # help dictionary d
    # d[a , b] = c  ==> if I want to find the smallest useful multiple of (30*pos)+a
    # on tkc, then I need the index given by the product of [(30*pos)+a][(30*pos)+b]
    # in general. If b < a, I need [(30*pos)+a][(30*(pos+1))+b]
    d = {}
    for x in offsets:
        for y in offsets:
            res = (x*y) % const
            if res in offsets:
                d[(x, res)] = y
    # another help dictionary: gives tkx calling tmptk[x]
    tmptk = {1:tk1, 7:tk7, 11:tk11, 13:tk13, 17:tk17, 19:tk19, 23:tk23, 29:tk29}
    pos, prime, lastadded, stop = 0, 0, 0, int(ceil(sqrt(N)))
    # inner functions definition
    def del_mult(tk, start, step):
        for k in lrange(start, len(tk), step):
            tk[k] = False
    # end of inner functions definition
    cpos = const * pos
    while prime < stop:
        # 30k + 7
        if tk7[pos]:
            prime = cpos + 7
            p.append(prime)
            lastadded = 7
            for off in offsets:
                tmp = d[(7, off)]
                start = (pos + prime) if off == 7 else (prime * (const * (pos + 1 if tmp < 7 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # 30k + 11
        if tk11[pos]:
            prime = cpos + 11
            p.append(prime)
            lastadded = 11
            for off in offsets:
                tmp = d[(11, off)]
                start = (pos + prime) if off == 11 else (prime * (const * (pos + 1 if tmp < 11 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # 30k + 13
        if tk13[pos]:
            prime = cpos + 13
            p.append(prime)
            lastadded = 13
            for off in offsets:
                tmp = d[(13, off)]
                start = (pos + prime) if off == 13 else (prime * (const * (pos + 1 if tmp < 13 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # 30k + 17
        if tk17[pos]:
            prime = cpos + 17
            p.append(prime)
            lastadded = 17
            for off in offsets:
                tmp = d[(17, off)]
                start = (pos + prime) if off == 17 else (prime * (const * (pos + 1 if tmp < 17 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # 30k + 19
        if tk19[pos]:
            prime = cpos + 19
            p.append(prime)
            lastadded = 19
            for off in offsets:
                tmp = d[(19, off)]
                start = (pos + prime) if off == 19 else (prime * (const * (pos + 1 if tmp < 19 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # 30k + 23
        if tk23[pos]:
            prime = cpos + 23
            p.append(prime)
            lastadded = 23
            for off in offsets:
                tmp = d[(23, off)]
                start = (pos + prime) if off == 23 else (prime * (const * (pos + 1 if tmp < 23 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # 30k + 29
        if tk29[pos]:
            prime = cpos + 29
            p.append(prime)
            lastadded = 29
            for off in offsets:
                tmp = d[(29, off)]
                start = (pos + prime) if off == 29 else (prime * (const * (pos + 1 if tmp < 29 else 0) + tmp) )//const
                del_mult(tmptk[off], start, prime)
        # now we go back to top tk1, so we need to increase pos by 1
        pos += 1
        cpos = const * pos
        # 30k + 1
        if tk1[pos]:
            prime = cpos + 1
            p.append(prime)
            lastadded = 1
            for off in offsets:
                tmp = d[(1, off)]
                start = (pos + prime) if off == 1 else (prime * (const * pos + tmp) )//const
                del_mult(tmptk[off], start, prime)
    # time to add remaining primes
    # if lastadded == 1, remove last element and start adding them from tk1
    # this way we don't need an "if" within the last while
    if lastadded == 1:
        p.pop()
    # now complete for every other possible prime
    while pos < len(tk1):
        cpos = const * pos
        if tk1[pos]: p.append(cpos + 1)
        if tk7[pos]: p.append(cpos + 7)
        if tk11[pos]: p.append(cpos + 11)
        if tk13[pos]: p.append(cpos + 13)
        if tk17[pos]: p.append(cpos + 17)
        if tk19[pos]: p.append(cpos + 19)
        if tk23[pos]: p.append(cpos + 23)
        if tk29[pos]: p.append(cpos + 29)
        pos += 1
    # remove exceeding if present
    pos = len(p) - 1
    while p[pos] > N:
        pos -= 1
    if pos < len(p) - 1:
        del p[pos+1:]
    # return p list
    return p



        
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step


def super_prime(first, last):
    primefix = ['2', '3', '5', '7']
        
    primes = sieve_wheel_30(last)
    total = 0
    for prime in primes:

        if prime < first:
            continue

        is_prime = True
        for x in str(prime):            
            if not x in primefix:
                is_prime = False
                break
        
        if is_prime: total += 1

    return total

import cProfile
cProfile.run("super_prime(1, 10000)")


