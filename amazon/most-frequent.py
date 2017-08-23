"""
a) Given an array of size n, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n. 
Find the maximum repeating number in this array. For example, let k be 10 the given array be 
arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2.
Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.

b) Write a O(n) time and O(1) extra space function that prints all maximum repeating elements. 

"""

import sys

array = [1, 3, 4, 5, 2, 2, 3, 2]
array = [2, 3, 3, 5, 3, 4, 1, 7]
array = [2, 3, 2, 3, 5]

k = len(array)

for i, v in enumerate(array):
    array[i] = v-1

for i, _ in enumerate(array):
    array[array[i] % k] += k


number = 0
max_number = 0

repeated_list = []
for i in range(k):
    repeated_list.append(array[i] // k)

for i in range(1, k):
    if max_number < repeated_list[i]:
        max_number = repeated_list[i]

final_list = []
for i in range(1, k):
    if max_number == repeated_list[i]:
        final_list.append(i+1)

print(final_list)