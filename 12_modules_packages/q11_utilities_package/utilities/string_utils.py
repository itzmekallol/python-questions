"""
string_utils.py — part of the utilities package.
"""


def reverse_string(s):
    return s[::-1]


def count_words(s):
    return len(s.split())


def to_uppercase(s):
    return s.upper()
