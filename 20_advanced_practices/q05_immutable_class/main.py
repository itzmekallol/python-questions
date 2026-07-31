"""
Q5: Custom immutable class — once an object is created, its attributes
cannot be modified.

Implemented by overriding __setattr__ to block all attribute
assignment after __init__ has finished, and __delattr__ to block
attribute deletion entirely.

Run with: python main.py
"""


class ImmutablePoint:
    def __init__(self, x, y):
        # object.__setattr__ bypasses our own blocking __setattr__ below,
        # which is required to set the initial values at all.
        object.__setattr__(self, "x", x)
        object.__setattr__(self, "y", y)
        object.__setattr__(self, "_initialized", True)

    def __setattr__(self, name, value):
        if getattr(self, "_initialized", False):
            raise AttributeError(
                f"Cannot modify attribute '{name}': {type(self).__name__} is immutable"
            )
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError(
            f"Cannot delete attribute '{name}': {type(self).__name__} is immutable"
        )

    def __repr__(self):
        return f"ImmutablePoint(x={self.x}, y={self.y})"


def main():
    print("Q5: Custom immutable class")

    point = ImmutablePoint(3, 5)
    print("Created:", point)

    try:
        point.x = 10
    except AttributeError as e:
        print("Caught error on attribute assignment:", e)

    try:
        del point.y
    except AttributeError as e:
        print("Caught error on attribute deletion:", e)

    print("Point remains unchanged:", point)


if __name__ == "__main__":
    main()
