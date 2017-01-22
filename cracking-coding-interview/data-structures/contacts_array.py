"""
    HackerRank
    Tries: Contacts (array version)
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
        self.__children = [None] * 26

    def getCharIndex(self, char):
        return ord(char) - ord('a')

    def getNode(self, char):
        return self.__children[self.getCharIndex(char)]
        
    def setNode(self, char, node):
        self.__children[self.getCharIndex(char)] = node

    def add(self, string, index=0):
        
        self.__size += 1

        if index == len(string):
            return

        char = string[index]
        child = self.getNode(char)
        if not child:
            child = Node()
            self.setNode(char, child)

        child.add(string, index + 1)

    def find(self, string, index=0):
        if index == len(string):
            return self.__size

        char = string[index]
        child = self.getNode(char)
        if not child:
            return 0
        
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



