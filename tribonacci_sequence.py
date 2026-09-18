
"""
The Tribonacci sequence is a series of numbers where each number 
is the sum of the three preceding ones. When starting with 0, 0 and 1,
the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers 
of a Tribonacci sequence, and an integer representing
the length of the sequence, return an array containing
the sequence of the given length.

Your function should handle sequences of any 
length greater than or equal to zero.

If the length is zero, return an empty array.

Note that the starting numbers are part of the sequence.

tribonacci_sequence([0, 0, 1], 20) should return 
[0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504,
 927, 1705, 3136, 5768, 10609, 19513]

tribonacci_sequence([21, 32, 43], 1) should return [21]

tribonacci_sequence([0, 0, 1], 0) should return []

tribonacci_sequence([10, 20, 30], 2) should return [10, 20]

tribonacci_sequence([10, 20, 30], 3) should return [10, 20, 30]

tribonacci_sequence([123, 456, 789], 8) should return
[123, 456, 789, 1368, 2613, 4770, 8751, 16134]
"""

def tribonacci_sequence(start_sequence, length):
    tri_seq = [0] * length
    a = start_sequence[0]
    b = start_sequence[1]
    c = start_sequence[2]

    for i in range(length):
        if i < 3:
            tri_seq[i] = start_sequence[i]
        else:
            tri_seq[i] = a + b + c
            a, b, c = b, c, tri_seq[i]

    return tri_seq
