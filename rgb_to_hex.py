"""
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.

rgb_to_hex("rgb(255, 255, 255)") should return "#ffffff"
rgb_to_hex("rgb(1, 11, 111)") should return "#010b6f"
rgb_to_hex("rgb(173, 216, 230)") should return "#add8e6"
rgb_to_hex("rgb(79, 123, 201)") should return "#4f7bc9"

"""


import re


def rgb_to_hex(rgb):
    # \d+ matches one or more digits
    numbers = re.findall(r'\d+', rgb)
    red, green, blue = [int(n) for n in numbers[:3]]
    
    return f"#{red:02x}{green:02x}{blue:02x}"