"""
book.py — part of the library package.
"""


class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_line(self):
        """Serialize this book as a comma-separated line for file storage."""
        return f"{self.book_id},{self.title},{self.author},{self.available}"

    @staticmethod
    def from_line(line):
        """Recreate a Book object from a stored comma-separated line."""
        book_id, title, author, available = line.strip().split(",")
        return Book(book_id, title, author, available == "True")

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"[{self.book_id}] '{self.title}' by {self.author} - {status}"
