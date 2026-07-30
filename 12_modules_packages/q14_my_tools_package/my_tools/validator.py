"""
validator.py — part of the my_tools package.
"""

import re


def is_valid_email(email):
    pattern = r"^[\w\.\-]+@[\w\-]+(\.[\w\-]+)*\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper and has_lower and has_digit and has_special
