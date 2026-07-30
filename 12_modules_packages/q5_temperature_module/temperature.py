"""
temperature.py — temperature conversion module.

Q5: Implements Celsius <-> Fahrenheit conversions.
"""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
