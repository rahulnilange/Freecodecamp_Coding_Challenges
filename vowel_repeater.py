

"""
Vowel Repeater

Given a string, return a new version of the string where 
each vowel is duplicated one more time than the previous 
vowel you encountered. For instance, the first vowel in 
the sentence should remain unchanged. The second vowel 
should appear twice in a row. The third vowel should 
appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase 
or lowercase, are considered vowels.

The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.

repeat_vowels("hello world") should return "helloo wooorld"
repeat_vowels("freeCodeCamp") should return "freeeCooodeeeeCaaaaamp"
repeat_vowels("AEIOU") should return "AEeIiiOoooUuuuu"
repeat_vowels("I like eating ice cream in Iceland") should return 
"I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"

"""


def repeat_vowels(s):
    new_s = ""
    vowel_counter = 0

    for letter in s:
        ## check if the letter is a vowel
        if letter in "aeiouAEIOU":
            vowel_counter += 1
            # then multiple the letter by
            # vowel_counter and then add
            # it to the string
            new_s += letter + (letter.lower()) * (vowel_counter - 1)
        else:
            # if the letter is not a vowel
            # then add letter itself
            new_s += letter
    return new_s
