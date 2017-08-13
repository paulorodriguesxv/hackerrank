
def is_mini_prime(number):

    while number:
        digit = number % 10

        if not digit in (2, 3, 5, 7):
            return False
        number //= 10

    return True

def isprime(number):
    maxv = number / 2 + 1 

    if number < 2:
        return False

    if not is_mini_prime(number): 
        return False

    i = 2
    while i < number // 2:
        
        if number % i != 0:
            i += 1
            continue
        resto = number / i 

        if resto <= i:
            return False

        i = resto
        
        return False
    """
    for i in xrange(2, maxv):        
        if number % i == 0:
            return False
    """        
    return True

def get_mega_primes(first, last):
    count = 0
    for x in xrange(first, last):
        if isprime(x): count += 1

    return count


print get_mega_primes(1, 1000)

import cProfile
#cProfile.run("get_mega_primes(1, 10000)") 

def cc():
    count = 0
    for i in xrange(1, 10**9):
        
        #digit = i % 10

        #if not digit in (2, 3, 5, 7):
        #    continue

        count +=1

    print count

cProfile.run("cc()") 
