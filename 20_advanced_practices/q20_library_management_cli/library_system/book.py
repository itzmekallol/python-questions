"""
book.py — Book data model.
"""


class Book:
    def __init__(self, book_id, title, author, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "copies": self.copies,
        }

    @staticmethod
    def from_dict(data):
        return Book(data["book_id"], data["title"], data["author"], data["copies"])

    def __str__(self):
        return f"[{self.book_id}] '{self.title}' by {self.author} - {self.copies} available"
