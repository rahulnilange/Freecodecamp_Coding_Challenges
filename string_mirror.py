

"""
String Mirror

Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.

is_mirror("helloworld", "helloworld") should return False
is_mirror("Hello World", "dlroW olleH") should return True
is_mirror("RaceCar", "raCecaR") should return True
is_mirror("RaceCar", "RaceCar") should return False
is_mirror("Mirror", "rorrim") should return False
is_mirror("Hello World", "dlroW-olleH") should return True
is_mirror("Hello World", "!dlroW !olleH") should return True

"""

import re

def is_mirror(str1, str2):
    # [^a-zA-Z] means "anything that is NOT a lowercase or uppercase letter"
    cleaned_string_1 = re.sub(r'[^a-zA-Z]', '', str1)
    cleaned_string_2 = re.sub(r'[^a-zA-Z]', '', str2)

    # reverse the second string, so that we can
    # do comparison of two strings
    string_2_reversed = cleaned_string_2[::-1]

    # check if the two strings are equal
    return cleaned_string_1 == string_2_reversed
