from itertools import product

matrix_a = [1, 2]
matrix_b = [3, 4]

products = product(matrix_a, matrix_b)


print(' '.join(map(str, products)))