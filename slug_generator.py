
"""
Given a string, return a URL-friendly 
version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.

Tests
generate_slug("helloWorld") should return "helloworld"
generate_slug("hello world!") should return "hello%20world"
generate_slug(" hello-world ") should return "helloworld"
generate_slug("hello  world") should return "hello%20world"
generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") should return "h3110%20w0r1d"

"""

import re

def generate_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r'\s+', '%20', text)
    return text
