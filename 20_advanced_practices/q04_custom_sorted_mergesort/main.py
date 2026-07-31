"""
Q4: Custom implementation of Python's built-in sorted() using the Merge
Sort algorithm. Supports ascending/descending order and a custom key
function, mirroring sorted()'s real signature.

Run with: python main.py
"""


def my_sorted(iterable, key=None, reverse=False):
    items = list(iterable)
    key_func = key if key is not None else (lambda x: x)
    sorted_items = _merge_sort(items, key_func)
    if reverse:
        sorted_items.reverse()
    return sorted_items


def _merge_sort(items, key_func):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], key_func)
    right = _merge_sort(items[mid:], key_func)
    return _merge(left, right, key_func)


def _merge(left, right, key_func):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main():
    print("Q4: Custom sorted() via Merge Sort")

    numbers = [8, 3, 1, 9, 4, 7, 2]
    print("Ascending:", my_sorted(numbers))
    print("Descending:", my_sorted(numbers, reverse=True))

    words = ["banana", "kiwi", "apple", "fig", "date"]
    print("\nBy length (ascending):", my_sorted(words, key=len))
    print("By length (descending):", my_sorted(words, key=len, reverse=True))

    people = [{"name": "Ravi", "age": 34}, {"name": "Meena", "age": 22}, {"name": "Suresh", "age": 45}]
    print("\nBy age using a custom key:")
    for person in my_sorted(people, key=lambda p: p["age"]):
        print(person)


if __name__ == "__main__":
    main()
