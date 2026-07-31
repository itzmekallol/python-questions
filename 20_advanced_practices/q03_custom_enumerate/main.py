"""
Q3: Custom implementation of Python's built-in enumerate() using a
generator function.

Run with: python main.py
"""


def my_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


def main():
    print("Q3: Custom enumerate()")

    fruits = ["apple", "banana", "cherry"]

    print("Default start (0):")
    for index, fruit in my_enumerate(fruits):
        print(index, fruit)

    print("\nCustom start (1):")
    for index, fruit in my_enumerate(fruits, start=1):
        print(index, fruit)


if __name__ == "__main__":
    main()
