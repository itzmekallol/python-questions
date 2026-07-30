"""
library.py — part of the library package.

Defines the Library class that ties Book, Member, and file_handler together.
"""

from library.book import Book
from library import file_handler


class Library:
    def __init__(self, data_file="library_data.txt"):
        self.data_file = data_file
        self.books = file_handler.load_books(self.data_file)
        self.members = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            return f"Book ID {book_id} already exists"
        self.books[book_id] = Book(book_id, title, author)
        self.save()
        return f"Book '{title}' added"

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_title = self.books[book_id].title
            del self.books[book_id]
            self.save()
            return f"Book '{removed_title}' removed"
        return "Book not found"

    def search_book(self, book_id):
        book = self.books.get(book_id)
        return str(book) if book else "Book not found"

    def display_books(self):
        return [str(book) for book in self.books.values()]

    def issue_book(self, book_id, member):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        if not book.available:
            return f"'{book.title}' is already issued"
        book.available = False
        member.borrow_book(book_id)
        self.save()
        return f"'{book.title}' issued to {member.name}"

    def return_book(self, book_id, member):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        book.available = True
        member.return_book(book_id)
        self.save()
        return f"'{book.title}' returned by {member.name}"

    def save(self):
        file_handler.save_books(self.data_file, self.books)
