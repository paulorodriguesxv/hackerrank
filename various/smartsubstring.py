#encoding: utf8

"""
"Smart substring" 
Write a function that takes maximum 30 characters from a string but without cutting the words. 

Full description: 
"Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam." 

First 30 characters: 
"Featuring stylish rooms and mo" 

Smarter approach (max 30 characters, no words are broken): 
"Featuring stylish rooms and"
"""


words = "Featuring stylish rooms and moorings for recreation boats, Room Mate Aitana is a designer hotel built in 2013 on an island in the IJ River in Amsterdam."


def takeWords2(awords, maxchars=30):

    splitedWords = awords.split()

    result = ""
    for word in splitedWords:

        if len(result) + len(word) <= maxchars:
            result += "%s " % word
        else:
            return result.strip()

print takeWords2(words, 30)
