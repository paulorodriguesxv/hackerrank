"""
    HackerRank
    https://www.hackerrank.com/challenges/ctci-find-the-running-median


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""


from Queue import PriorityQueue


class PriorityQueueEx(object):

    def __init__(self, inverse=False):
        self._inverse = inverse
        self._data = PriorityQueue()

    def peek(self):
        return self._data.queue[0][1]

    def empty(self):
        return self._data.empty()

    def size(self):
        return self._data.qsize()

    def put(self, item):

        if self._inverse:
            self._data.put((-item, item))
        else:
            self._data.put((item, item))

    
    def pop(self):
        return abs(self._data.get()[1])

class Solution(object):

    def addNumber(self, number, lowers, highers):

        if lowers.empty() or number < lowers.peek():
            lowers.put(number)
        else:
            highers.put(number)

    def rebalance(self, lowers, highers):

        biggerHeap = lowers if lowers.size() > highers.size() else highers
        smallerHeap = highers if lowers.size() > highers.size() else lowers

        if biggerHeap.size() - smallerHeap.size() >= 2:
            smallerHeap.put(biggerHeap.pop())

    def getMedian(self, lowers, highers):
    
        biggerHeap = lowers if lowers.size() > highers.size() else highers
        smallerHeap = highers if lowers.size() > highers.size() else lowers

        if biggerHeap.size() == smallerHeap.size():
            return  (biggerHeap.peek() + smallerHeap.peek()) / 2.0
        else:
            return biggerHeap.peek() * 1.0

    def getMedians(self, numbers):
        lowers = PriorityQueueEx(inverse=True)
        highers = PriorityQueueEx()

        medians = []

        for number in numbers:
            self.addNumber(number, lowers, highers)
            self.rebalance(lowers, highers)
            medians.append(self.getMedian(lowers, highers))

        return medians


med = Solution()
print med.getMedians([12, 4, 5, 3, 8, 7])

