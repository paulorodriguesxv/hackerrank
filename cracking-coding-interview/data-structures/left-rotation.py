"""
    HackerRank
    https://www.hackerrank.com/challenges/ctci-array-left-rotation


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

def array_left_rotation(a, n, k):
 
    return a[k:] + a[:k]


print array_left_rotation([1,2,3,4,5], 5, 2)