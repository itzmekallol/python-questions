"""
geometry.py — geometry calculations module.

Q2: Implements area functions for circle, rectangle, and triangle.
"""

PI = 3.14159


def area_of_circle(radius):
    return round(PI * radius ** 2, 2)


def area_of_rectangle(length, width):
    return length * width


def area_of_triangle(base, height):
    return 0.5 * base * height
