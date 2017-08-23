"""
    HackerRank
    https://www.hackerrank.com/challenges/ctci-making-anagrams


    Paulo Leonardo Vieira Rodrigues 
    https://github.com/paulorodriguesxv
    Brazil - 2017
    
"""

from collections import Counter

a = "fcrxzwscanmligyxyvy"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeok"

lista = Counter(a)
listb = Counter(b)

diff = 0
for key in listb:
    if key not in lista:
        diff += listb[key]
    else:
        diff += max(0, listb[key] - lista[key])

for key in lista:
    if key not in listb:
        diff += lista[key]
    else:
        diff += max(0, lista[key] - listb[key])

print(diff)