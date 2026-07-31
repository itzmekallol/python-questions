"""
library.py — the core Library class that ties book, member,
transaction, storage, and logger together.
"""

from datetime import datetime

from library_system.book import Book
from library_system.member import Member
from library_system.transaction import Transaction
from library_system.storage import Storage


class LibraryError(Exception):
    """Base exception for all library-related errors."""
    pass


class BookNotFoundError(LibraryError):
    pass


class DuplicateBookIDError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class DuplicateMemberIDError(LibraryError):
    pass


class NoCopiesAvailableError(LibraryError):
    pass


class Library:
    def __init__(self, filename, logger=None):
        self.storage = Storage(filename)
        self.logger = logger
        raw_data = self.storage.load()

        self.books = {bid: Book.from_dict(b) for bid, b in raw_data.get("books", {}).items()}
        self.members = {mid: Member.from_dict(m) for mid, m in raw_data.get("members", {}).items()}
        self.transactions = [Transaction.from_dict(t) for t in raw_data.get("transactions", [])]

        self._log("Library system initialized")

    def _log(self, message):
        if self.logger:
            self.logger.info(message)

    def _save(self):
        data = {
            "books": {bid: b.to_dict() for bid, b in self.books.items()},
            "members": {mid: m.to_dict() for mid, m in self.members.items()},
            "transactions": [t.to_dict() for t in self.transactions],
        }
        self.storage.save(data)

    # ----- Book management -----
    def add_book(self, book_id, title, author, copies=1):
        if book_id in self.books:
            raise DuplicateBookIDError(f"Book ID '{book_id}' already exists")
        self.books[book_id] = Book(book_id, title, author, copies)
        self._save()
        self._log(f"Book added: {book_id} - '{title}'")
        return f"Book '{title}' added"

    def search_book(self, keyword):
        keyword_lower = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword_lower in book.title.lower() or keyword_lower in book.author.lower()
        ]

    # ----- Member management -----
    def add_member(self, member_id, name):
        if member_id in self.members:
            raise DuplicateMemberIDError(f"Member ID '{member_id}' already exists")
        self.members[member_id] = Member(member_id, name)
        self._save()
        self._log(f"Member added: {member_id} - '{name}'")
        return f"Member '{name}' added"

    # ----- Issue / return -----
    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if not book:
            raise BookNotFoundError(f"Book '{book_id}' not found")
        if not member:
            raise MemberNotFoundError(f"Member '{member_id}' not found")
        if book.copies <= 0:
            raise NoCopiesAvailableError(f"No copies of '{book.title}' available")

        book.copies -= 1
        member.borrowed_books.append(book_id)
        self.transactions.append(Transaction(member_id, book_id, "issue"))
        self._save()
        self._log(f"Book issued: {book_id} to member {member_id}")
        return f"'{book.title}' issued to {member.name}"

    def return_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if not book:
            raise BookNotFoundError(f"Book '{book_id}' not found")
        if not member:
            raise MemberNotFoundError(f"Member '{member_id}' not found")
        if book_id not in member.borrowed_books:
            raise LibraryError(f"Member '{member.name}' has not borrowed book '{book_id}'")

        book.copies += 1
        member.borrowed_books.remove(book_id)
        self.transactions.append(Transaction(member_id, book_id, "return"))
        self._save()
        self._log(f"Book returned: {book_id} from member {member_id}")
        return f"'{book.title}' returned by {member.name}"

    # ----- Reporting -----
    def transaction_history(self, member_id=None):
        if member_id:
            return [t for t in self.transactions if t.member_id == member_id]
        return list(self.transactions)

    def display_all_books(self):
        return list(self.books.values())
