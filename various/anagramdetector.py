"""

Problem:

An anagram is a word that can be written as a permutation of the characters of another word, like "dirty room" and "dormitory" (ignore spaces). However, "the" and "thee" are not anagrams, since "the" only has a single "e" whereas "thee" has two "e" characters (spaces can occur zero, or multiple times, however.)

Given a list of words as strings, you should return another list of strings, each containing words that are mutual anagrams.

Each string of the output should be a single group of anagarms joined with commas.

Within an output string, the expression should be sorted lexicographically. If a group contains only a single element, output that one-element group as a single string. And the string should be also output in lexicographical order. Given e.g.:

pear
amleth
dormitory
tinsel
dirty room
hamlet
listen
silnet
... the output would be:

amleth,hamlet
dirty room,dormitory
listen,silnet,tinsel
pear

"""


anagrams = ['pear', 'amleth', 'dormitory', 'tinsel', 'dirty room', 'hamlet', 'listen', 'silnet']
sortedAnagrams = [''.join(sorted(x)).replace(' ', '') for x in anagrams]

resultAnagrams = {}

for i, ana in enumerate(sortedAnagrams):
    key = ana.replace(' ', '')
    if resultAnagrams.has_key(key):
        resultAnagrams[key].append(anagrams[i])
    else:
        resultAnagrams[key] = [anagrams[i]]

print resultAnagrams.values()