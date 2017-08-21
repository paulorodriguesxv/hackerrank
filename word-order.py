"""
https://www.hackerrank.com/challenges/word-order?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""
from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):

     def __repr__(self):
         return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

     def __reduce__(self):
         return self.__class__, (OrderedDict(self),)    

words_counter = int(input().strip())
words = []
for i in range(words_counter):
    words.append(input().strip())

words_list = OrderedCounter(words)
print(len(words_list))
for word in words_list:
    print(words_list[word], end=" ")