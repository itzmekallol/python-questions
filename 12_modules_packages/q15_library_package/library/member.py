"""
member.py — part of the library package.
"""


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}) - Borrowed: {self.borrowed_books}"
