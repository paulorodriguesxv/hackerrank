def sieveOfEratosthenes(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


count = 0
for x in sieveOfEratosthenes(100000):
    count += 1

print(count)                