"""
Remove the duplicates from the array without extra space.
"""

arr = [4, 2, 1, 5, 1, 3, 1]

for i, value in enumerate(arr):

    if arr[abs(value)] > 0:
        arr[abs(value)] = -arr[abs(value)]         
    else:
        print("dupicate: ", abs(value))


    print(arr)