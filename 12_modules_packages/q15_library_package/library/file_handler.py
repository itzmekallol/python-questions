"""
file_handler.py — part of the library package.

Handles saving and loading book records to/from a text file.
"""

import os


def save_books(filename, books):
    with open(filename, "w") as f:
        for book in books.values():
            f.write(book.to_line() + "\n")


def load_books(filename):
    from library.book import Book  # local import avoids a circular import at module load time

    books = {}
    if not os.path.exists(filename):
        return books
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                book = Book.from_line(line)
                books[book.book_id] = book
    return books
