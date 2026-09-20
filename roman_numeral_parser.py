

"""
Roman Numeral Parser

Given a string representing a Roman numeral, return its integer value.
Roman numerals consist of the following symbols and values:

Symbol -- Value
I      -- 1
V      -- 5
X      -- 10
L      -- 50
C      -- 100
D      -- 500
M      -- 1000

Numerals are read left to right. If a smaller numeral 
appears before a larger one, the value is subtracted. Otherwise, values are added.

parse_roman_numeral("III") should return 3
parse_roman_numeral("IV") should return 4
parse_roman_numeral("XXVI") should return 26
parse_roman_numeral("XCIX") should return 99
parse_roman_numeral("CDLX") should return 460
parse_roman_numeral("DIV") should return 504
parse_roman_numeral("MMXXV") should return 2025

"""

def parse_roman_numeral(numeral):
    roman_dict = {
        "I" : 1,
        "V":  5,
        "X":  10,
        "L":  50,
        "C":  100,
        "D":  500,
        "M":  1000
    }

    # initialize the value
    total = 0

    # start iterating through the string
    for i, letter in enumerate(numeral):
        if i == (len(numeral) - 1):
            total += roman_dict[letter]
        else:
            next_char = numeral[i + 1]
            if roman_dict[letter] < roman_dict[next_char]:
                    total -= roman_dict[letter]
            else:
                total += roman_dict[letter]

    return total


