"""
password_generator.py — part of the my_tools package.
"""

import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))
