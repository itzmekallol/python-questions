"""
main.py — imports string_utils using an alias.

Q4: Demonstrates "import module as alias".

Run with: python main.py
"""

import string_utils as su

print("Q4: Using string_utils via the alias 'su'")
print("Reversed 'python':", su.reverse_string("python"))
print("'Madam' is palindrome:", su.is_palindrome("Madam"))
print("Vowel count in 'Programming':", su.count_vowels("Programming"))
print("Title case of 'hello world':", su.to_title_case("hello world"))
