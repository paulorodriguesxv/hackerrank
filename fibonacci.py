def fibonacci(n):
    a, b = 1, 1
    for x in range(n):
       yield a
       a,b = b,a+b

f = fibonacci(10)
for x in f:
    print(x)