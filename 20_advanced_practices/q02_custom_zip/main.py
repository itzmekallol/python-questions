"""
Q2: Custom implementation of Python's built-in zip(), supporting any
number of iterables. Implemented as a generator so it stays lazy, just
like the real zip().

Run with: python main.py
"""


def my_zip(*iterables):
    iterators = [iter(iterable) for iterable in iterables]
    while True:
        result = []
        for iterator in iterators:
            try:
                result.append(next(iterator))
            except StopIteration:
                return  # stop as soon as ANY iterable is exhausted, like real zip()
        yield tuple(result)


def main():
    print("Q2: Custom zip()")

    names = ["Aarav", "Isha", "Vikram"]
    ages = [20, 21, 19]
    cities = ["Kolkata", "Mumbai", "Delhi"]

    print("Two iterables:")
    for pair in my_zip(names, ages):
        print(pair)

    print("\nThree iterables:")
    for triple in my_zip(names, ages, cities):
        print(triple)

    print("\nUnequal lengths (stops at the shortest):")
    for pair in my_zip([1, 2, 3, 4, 5], ["a", "b", "c"]):
        print(pair)


if __name__ == "__main__":
    main()
