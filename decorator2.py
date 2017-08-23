"""
https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
"""

from operator import itemgetter
def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
                
        for person in people:
            yield f(person)
        return people
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [  ['Jake','Jake',42,'M'],
                ['Jake','Kevin',57,'M'],
                ['Jake','Michael',91,'M'],
                ['Kevin','Jake',2,'M'],
                ['Kevin','Kevin',44,'M'],
                ['Kevin','Michael',100,'M'],
                ['Michael','Jake',4,'M'],
                ['Michael','Kevin',36,'M'],
                ['Michael','Michael',15,'M'],
                ['Micheal','Micheal',6,'M']]
    print(*name_format(people), sep='\n')