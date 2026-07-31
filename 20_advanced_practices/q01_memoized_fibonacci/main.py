"""
Q1: Memoized Fibonacci function without external libraries.

Stores previously computed values in a dictionary so repeated calls
(and the recursive sub-calls within a single call) are O(1) after the
first computation, instead of the exponential blow-up of naive
recursive Fibonacci.

Run with: python main.py
"""


def make_memoized_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def main():
    fibonacci = make_memoized_fibonacci()
    print("Q1: Memoized Fibonacci")
    for i in range(11):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    print("fibonacci(50) =", fibonacci(50))  # instant, thanks to memoization


if __name__ == "__main__":
    main()
