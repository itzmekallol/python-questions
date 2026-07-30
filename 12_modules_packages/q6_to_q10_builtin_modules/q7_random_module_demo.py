"""
q7_random_module_demo.py

Q7: Uses the random module to generate a random integer, a random
float, pick a random item from a list, and shuffle a list.
"""

import random

random.seed(42)  # seeded so the demo output is reproducible

print("Q7: Built-in random module")
print("Random integer (1-100):", random.randint(1, 100))
print("Random float (0-1):", random.random())

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]
print("Random item from list:", random.choice(fruits))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)
