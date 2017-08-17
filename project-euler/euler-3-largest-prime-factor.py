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

n = 17
primes = sieveOfEratosthenes(n)

def get_largest_prime(primes, number):
    for i, x in enumerate(primes):
        if i < 2: continue
        if x and  number % i == 0:
            yield i

prime = 0
for prime in get_largest_prime(primes, n):
    pass

print(prime)



