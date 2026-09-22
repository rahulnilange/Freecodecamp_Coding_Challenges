
"""
Acronym Builder

Given a string containing one or more words, 
return an acronym of the words using the following constraints:

The acronym should consist of the first letter 
of each word capitalized, unless otherwise noted.

The acronym should ignore the first letter of 
these words unless they are the first word 
of the given string: a, for, an, and, by, and of.

The acronym letters should be returned in the order they are given.

The acronym should not contain any spaces.

build_acronym("Search Engine Optimization") should return "SEO"
build_acronym("Frequently Asked Questions") should return "FAQ"
build_acronym("National Aeronautics and Space Administration") should return "NASA"
build_acronym("Federal Bureau of Investigation") should return "FBI"
build_acronym("For your information") should return "FYI"
build_acronym("By the way") should return "BTW"
build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily") 
should return "AUHWPOTIMSH"

"""


def build_acronym(s):
    avoid_words = {'a', 'for', 'an', 'and', 'by', 'of'}
    word_list = s.lower().split()
    abbr_str = ""

    for index, word in enumerate(word_list):
        if (word in avoid_words) and (index == 0):
            abbr_str += word[0].upper()
        elif (word not in avoid_words):
            abbr_str += word[0].upper()

    return abbr_str

