
"""
Unique Characters

Given a string, determine if all the 
characters in the string are unique.

Uppercase and lowercase letters should 
be considered different characters.

all_unique("abc") should return True
all_unique("aA") should return True
all_unique("QwErTy123!@") should return True
all_unique("~!@#$%^&*()_+") should return True
all_unique("hello") should return False
all_unique("freeCodeCamp") should return False
all_unique("!@#*$%^&*()aA") should return False
"""

def all_unique(s):
    return len(s) == len(set(s))