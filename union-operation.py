"""
https://www.hackerrank.com/challenges/py-set-union?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""
english_count = int(input().strip())
english_students = set([int(x) for x in input().split()])

french_count = int(input().strip())
french_students = set([int(x) for x in input().split()])

students = english_students | french_students

print(len(students))
