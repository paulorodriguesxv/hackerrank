"""
    HackerRank
    Tries: Contacts (hash version)
    This implementation use a lot of memory space, and hackerrank vm have limited memory. 
    For this approach, you should use a python __slots__ to optimize memory allocation
    
    https://www.hackerrank.com/challenges/ctci-contacts


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

class Node(object):

    __slots__ = ["__children", "__size"]

    def __init__(self):
        self.__size = 0
        self.__children = {}

    def add(self, string, index=0):

        self.__size += 1

        if index == len(string):
            return

        char = string[index]

        if not self.__children.has_key(char):
            child = Node()
            self.__children[char] = child
        else:
            child = self.__children[char]

        child.add(string, index + 1)

    def find(self, string, index=0):
        if index == len(string):
            return self.__size

        char = string[index]

        if not self.__children.has_key(char):
            return 0
        else:
            child = self.__children[char]

        return child.find(string, index + 1)



f = open("contacts.txt")
n = int(f.readline().strip())

root = Node()
for a0 in xrange(n):
    op, contact = f.readline().strip().split(' ')

    if op == "add":
        root.add(contact)
    if op == "find":
        root.find(contact)



