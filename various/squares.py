"""
$a = [3, 1, 4, 5, 19, 6];

$b = [14, 9, 22, 36, 8, 0, 64, 25];
# Some elements in the second array are squares. 
# Print elements that have a square root existing in the first array. 
# $b[1] = 9, its square root is 3 ($a[0]) 
# $b[3] = 36, its square root is 6 ($a[5]) 
# $b[7] = 25, its square root is 5 ($a[3]) 

# Result: 
# 9 
# 36 
# 25

"""

import math

squares = [3, 1, 4, 5, 19, 6]
numbers = [14, 9, 22, 36, 8, 0, 64, 25]

sqEqual = lambda: [x for x in numbers if math.sqrt(x) in squares]

print sqEqual()