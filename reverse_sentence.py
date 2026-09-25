
"""
Reverse Sentence

Given a string of words, return a new string with 
the words in reverse order. For example, the first 
word should be at the end of the returned string, 
and the last word should be at the beginning of the 
returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.

reverse_sentence("world hello") should return "hello world"
reverse_sentence("push commit git") should return "git commit push"
reverse_sentence("npm  install   apt    sudo") should return "sudo apt install npm"
reverse_sentence("import    default   function  export") 
should return "export function default import"

"""

def reverse_sentence(sentence):
    # create a list of words in the
    # sentence. 
    sentence_list = sentence.split()
    # reverse this list
    sentence_list.reverse()
    # create the sentence from this list
    new_sentence = " ".join(sentence_list)
    return new_sentence


