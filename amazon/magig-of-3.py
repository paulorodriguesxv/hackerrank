"""
1. Magic of 3

A number ending with 3 will have a multiple which is all 1. Eg­ multiple of 3 is 111 and of

13 is 111111. Given a number ending with 3 find its least multiple which is all 1. The

2 multiple of the given number can be beyond the range of int,long etc. Optimize for time.
"""


count = 1
rem = 1
n = 13
while (rem):
    rem= (rem*10+1) % n
    count += 1

while (count):
    count -= 1
    print("1")