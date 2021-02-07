import urllib.parse


def multiply(a, b):
    return a + b


def convert_string(s):
    return s[::-1]


def validate_input(s):
    s = urllib.parse.quote(s, safe='')
    return s[:50]
