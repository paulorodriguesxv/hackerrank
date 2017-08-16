import math

def sieveOfEratosthenes(maxi):
    flags = [True] * (maxi + 1)
    prime = 2

    flags[0] = False
    flags[1] = False
    
    while (prime <= math.sqrt(maxi) ):
        crossOff(flags, prime)

        prime = getNexPrime(flags, prime)

    return flags

def crossOff(flags, prime):

    for i in range(prime*prime, len(flags), prime):
        flags[i] = False

def getNexPrime(flags, prime):
    nexti = prime + 1
    while (nexti < len(flags) and (not flags[nexti])):
        nexti +=1

    return nexti

count = 0
for x in sieveOfEratosthenes(100000):
    if x: count += 1

print(count)