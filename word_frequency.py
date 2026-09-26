
"""
Word Frequency

Given a paragraph, return an array of the 
three most frequently occurring words.

Words in the paragraph will be separated by spaces.

Ignore case in the given paragraph. 
For example, treat Hello and hello as the same word.

Ignore punctuation in the given paragraph. 
Punctuation consists of commas (,), 
periods (.), and exclamation points (!).

The returned array should have all lowercase words.

The returned array should be in descending order with 
the most frequently occurring word first.

get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")
= ["coding", "python", "in"]

get_words("I like coding. I like testing. I love debugging!") 
= ["i", "like", "coding"]

get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!")
= ["debug", "test", "deploy"]

"""


import re
from collections import Counter

def get_words(paragraph):
    # [a-z]+ matches one or more lowercase letters only
    # words is a list where elements are words
    # from the paragraph excluding non alphabetical
    # characters
    words = re.findall(r'[a-z]+', paragraph.lower())

    # Get the frequency count
    counts = Counter(words)

    # Arrange in descending order of frequency
    # sorted_counts is a list of tuples
    # this will get a list of three tuples
    sorted_counts = counts.most_common(3)

    # get top 3 words from tuples
    top_three_words = [word for word, count in sorted_counts]

    return top_three_words


