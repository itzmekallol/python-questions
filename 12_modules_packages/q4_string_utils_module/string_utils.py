"""
string_utils.py — string utility functions module.

Q4: Implements reverse string, palindrome check, vowel count, title case.
"""


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def to_title_case(s):
    return s.title()
