"""
Merge two sorted array into a single sorted array. No extra space are allowed.

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20} 

"""



a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]


def merge(ar1, ar2):

    m = len(ar1)
    n = len(ar2)

    """ 
        Iterate through all elements of ar2[] starting from
    the last element
    """  
    for i in range(n-1, -1, -1):
        """ 
            Find the smallest element greater than ar2[i]. Move all
            elements one position ahead till the smallest greater
            element is not found
        """
        last = ar1[m-1]

        j = m - 2
        while (j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j -= 1
 
        # If there was a greater element
        if (j != m-2 or last > ar2[i]):
            ar1[j+1] = ar2[i]
            ar2[i] = last


merge(a, b)

print(a + b)