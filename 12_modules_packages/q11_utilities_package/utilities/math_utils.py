"""
math_utils.py — part of the utilities package.
"""


def square(number):
    return number ** 2


def cube(number):
    return number ** 3


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
