


"""
Perfect Square

Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an 
integer by itself to achieve the number. 
For example, 9 is a perfect square because 
you can multiply 3 by itself to get it.

is_perfect_square(9) should return True
is_perfect_square(49) should return True
is_perfect_square(1) should return True
is_perfect_square(2) should return False
is_perfect_square(99) should return False
is_perfect_square(-9) should return False
is_perfect_square(0) should return True
is_perfect_square(25281) should return True
"""


def is_perfect_square(n):
    if n < 0:
        return False

    # Find the integer square root
    root = int(n ** 0.5)

    # Check if the square of the root equals the original number
    return (root * root) == n