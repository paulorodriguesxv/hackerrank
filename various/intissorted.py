

def issorted(arr):
    priorNumber = arr[0]

    for number in arr:
        if  priorNumber > number:
            return "not sorted"

        priorNumber = number

    return "sorted"


mylist = [1,1,2,3,5,6,7]
print issorted(mylist)