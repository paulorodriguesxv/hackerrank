"""
    HackerRank
    https://www.hackerrank.com/challenges/ctci-ransom-note


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

a = "give me one grand today nigh".split()
b = "give one grand today".split()

#a = "o l x imjaw bee khmla v o v o imjaw l khmla imjaw x".split()
#b = "imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o".split()

from collections import Counter
def ransom_note(magazine, rasom):

    magazine = Counter(magazine)
    rasomresult = []
    for ra in rasom:
        if ra in magazine and magazine[ra] > 0:
            magazine[ra] -= 1
            rasomresult.append(ra)
    
    return rasomresult == rasom
print ransom_note(a, b)