

def is_palindrome(number):
    nreversed = 0
    n = number

    while (n > 0):
        nreversed = nreversed * 10 + n % 10
        n //= 10

    print(number)
    print(nreversed)
    return number == nreversed

def get_palindrome(limit):
    max_palindrome = 0
    for n1 in range(999, 100, -1):
        for n2 in range(999, n1-1, -1):
            ts = n1 * n2

            if ts > limit: continue
            if ts <= max_palindrome: break
            
            if ts <= limit and (str(ts) == str(ts)[::-1]):
                if ts > max_palindrome:
                    max_palindrome = ts                    
            
            n2 -= 1
        
        n1 -= 1

    return max_palindrome
print(get_palindrome(800000))

