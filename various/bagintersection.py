# encoding: utf8
"""
A multiset or a bag is a collection of elements that can be repeated. Contrast with a set, where elements cannot be repeated. 
Multisets can be intersected just like sets can be intersected. 

Input : 

A = [0,1,1,2,2,5] 
B = [0,1,2,2,2,6] 

Output : 
A ∩ B = C = [0,1,2,2] 

Input : 
A = [0,1,1] 
B = [0,1,2,3,4,5,6] 

Output 
A ∩ B = C = [0,1] 

Write a function to find the intersection of two integer arrays in that way ?
"""

from collections import Counter

def intersection(dictA, dictB):

    intersectResult = []
    counterA = Counter(dictA) 
    counterB = Counter(dictB)

    intersectDict =  counterA & counterB

    for key in intersectDict.keys():
        qtd = intersectDict[key]
        for x in xrange(qtd):
            intersectResult.append(key)

    return intersectResult

a = [0,1,1,2,2,5]
b = [0,1,2,2,2,6]

print intersection(a, b)

a = [0,1,1]
b = [0,1,2,3,4,5,6]

print intersection(a, b)

