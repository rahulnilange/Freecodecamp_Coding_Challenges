"""
Array Diff

Given two arrays with strings values, return a new 
array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.

array_diff(["apple", "banana"], ["apple", "banana", "cherry"])
should return ["cherry"]

array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) 
should return ["cherry"]

array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]) 
should return ["eight", "four", "six", "two"]

array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]) 
should return ["five", "one", "seven", "three"]

array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) 
should return ["freeCodeCamp", "rocks"]

"""


def array_diff(arr1, arr2):
    result = list(set(arr1) ^ set(arr2))
    result.sort()
    return result
