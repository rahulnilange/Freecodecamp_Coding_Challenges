
"""
Missing Numbers

Given an array of integers from 1 to n, inclusive, 
return an array of all the missing integers 
between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.

find_missing_numbers([1, 3, 5]) = [2, 4]
find_missing_numbers([1, 2, 3, 4, 5]) = []
find_missing_numbers([1, 10]) = [2, 3, 4, 5, 6, 7, 8, 9]
find_missing_numbers([10, 1, 10, 1, 10, 1]) = 
[2, 3, 4, 5, 6, 7, 8, 9]

find_missing_numbers([3, 1, 4, 1, 5, 9]) = [2, 6, 7, 8]
find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4])
= [11]

"""

def find_missing_numbers(arr):
    # handle empty array case
    if not arr:
        return []
    # since 1 is already included in
    # the list, we need to find n,
    # which is the max element
    n = max(arr)
    
    # create a set from 1 to n
    set_1_to_n = set(range(1, n+1))
    # create a set from array
    set_arr = set(arr)
    # Subtract sets and return a sorted list instantly
    return sorted(set_1_to_n - set_arr)

