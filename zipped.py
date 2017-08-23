"""
    https://www.hackerrank.com/challenges/zipped/problem
"""
n, m = map(int, input().split())

students = zip(*[[float(x) for x in input().split()] for i in range(m)])

for x in students:
    print(sum(x) / m)