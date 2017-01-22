"""
    HackerRank
    Tries: Contacts (collections version, using chained dictonaries)
    This version doesn't need to use __slots__ to pass the tests on hackerrank

    https://www.hackerrank.com/challenges/ctci-contacts


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

from collections import defaultdict

SIZE_ATTR = 'size'

def Node():
    return defaultdict(Node)


def add(node, string):
    if SIZE_ATTR not in node:
        node[SIZE_ATTR] = 0

    node[SIZE_ATTR] += 1

    if string:
        char = string[0]
        add(node[char], string[1:])
    
def find(node, string):
    if string and node:
        return find(node[string[0]], string[1:])
    else:
        return node.get(SIZE_ATTR, 0)

f = open("contacts.txt")
n = int(f.readline().strip())

contacts = Node()
for a0 in xrange(n):
    op, contact = f.readline().strip().split(' ')

    if op == "add":
        add(contacts, contact)
    if op == "find":
        print find(contacts, contact)
