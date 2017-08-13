"""
Given a stream of characters (e.g. acacabcatghhellomvnsdb) and a list of words (e.g. ["aca","cat","hello","world"] ) 
find and display count of each and every word once the stream ends.
(Like : "aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0 ).
"""

def countWorlds(wordList, charInput):

    countedWords = {x:0 for x in wordList}

    for word in wordList:
        pos = charInput.find(word)

        while pos >= 0:
            countedWords[word] += 1
            pos = charInput.find(word, pos + 1)

    return countedWords

words = ["aca","cat","hello","world"]
print countWorlds(words, 'acacabcatghhellomvnsdb')
