"""
There's a very simple compression algorithm that takes subsequent characters and just emits how often they were seen. 

Example: 
abababaabbbaaaaa
"""

from collections import defaultdict

stream = 'abababaabbbaaaaa'

finalList = ""
count = 1
actualLetter = stream[0]

for letter in stream:

    if actualLetter == letter:
        count += 1
    else:
        finalList += "%s%d" % (actualLetter, count)
        count = 1

    actualLetter = letter

finalList += "%s%d" % (actualLetter, count)
print finalList

