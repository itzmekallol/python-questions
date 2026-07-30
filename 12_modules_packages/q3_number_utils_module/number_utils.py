"""
number_utils.py — number utility functions module.

Q3: Implements even/odd check, prime check, reverse a number, count digits.
"""


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def reverse_number(number):
    temp = abs(number)
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    return reversed_num if number >= 0 else -reversed_num


def count_digits(number):
    temp = abs(number)
    if temp == 0:
        return 1
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    return count
