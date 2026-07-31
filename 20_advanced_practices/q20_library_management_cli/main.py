"""
main.py — entry point for the Command-Line Library Management System.

Q20: Professional Library Management System.

Structure:
    q20_library_management_cli/
    ├── library_system/
    │   ├── __init__.py
    │   ├── book.py
    │   ├── member.py
    │   ├── transaction.py
    │   ├── storage.py
    │   ├── logger.py
    │   └── library.py
    └── main.py   (this file)

Run with: python main.py

The real interactive menu loop is included as a comment inside
run_menu(); underneath it, a scripted demo exercises every feature
(search, issue/return, past-date rejection, transaction history,
logging) so the program runs end-to-end without manual entry.
"""

import os
from datetime import date, timedelta

from library_system.library import (
    Library,
    BookNotFoundError,
    DuplicateBookIDError,
    MemberNotFoundError,
    DuplicateMemberIDError,
    NoCopiesAvailableError,
    LibraryError,
)
from library_system.logger import get_logger

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


def run_menu():
    """
    Real interactive version:

    while True:
        print('''
        1. Add Book
        2. Add Member
        3. Search Book
        4. Issue Book
        5. Return Book
        6. Display All Books
        7. Transaction History
        8. Exit
        ''')
        choice = input("Choose an option: ")
        try:
            if choice == "8":
                print("Goodbye!")
                break
            elif choice == "1":
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                copies = int(input("Copies: "))
                print(library.add_book(book_id, title, author, copies))
            elif choice == "2":
                member_id = input("Member ID: ")
                name = input("Name: ")
                print(library.add_member(member_id, name))
            elif choice == "3":
                keyword = input("Search keyword: ")
                for book in library.search_book(keyword):
                    print(book)
            elif choice == "4":
                book_id = input("Book ID: ")
                member_id = input("Member ID: ")
                print(library.issue_book(book_id, member_id))
            elif choice == "5":
                book_id = input("Book ID: ")
                member_id = input("Member ID: ")
                print(library.return_book(book_id, member_id))
            elif choice == "6":
                for book in library.display_all_books():
                    print(book)
            elif choice == "7":
                for txn in library.transaction_history():
                    print(txn)
        except LibraryError as e:
            print("Error:", e)
    """
    logger = get_logger(DATA_DIR)
    library = Library(path("library_data.json"), logger=logger)

    print("Q20: Command-Line Library Management System")
    print("(Running a scripted demo of every feature)\n")

    print(library.add_book("B1", "The Hobbit", "J.R.R. Tolkien", copies=2))
    print(library.add_book("B2", "1984", "George Orwell", copies=1))
    print(library.add_book("B3", "Brave New World", "Aldous Huxley", copies=1))

    try:
        library.add_book("B1", "Duplicate Attempt", "Someone", copies=1)
    except DuplicateBookIDError as e:
        print("Caught error:", e)

    print(library.add_member("M1", "Priya"))
    print(library.add_member("M2", "Rahul"))

    print("\nSearching for 'orwell':")
    for book in library.search_book("orwell"):
        print(book)

    print("\n" + library.issue_book("B2", "M1"))
    try:
        library.issue_book("B2", "M2")  # only 1 copy existed, now 0 left
    except NoCopiesAvailableError as e:
        print("Caught error:", e)

    try:
        library.issue_book("B99", "M1")  # nonexistent book
    except BookNotFoundError as e:
        print("Caught error:", e)

    print("\n" + library.return_book("B2", "M1"))
    print(library.issue_book("B2", "M2"))  # now available again

    print("\nAll books:")
    for book in library.display_all_books():
        print(book)

    print("\nTransaction history:")
    for txn in library.transaction_history():
        print(txn)

    print("\nTransaction history for M1 only:")
    for txn in library.transaction_history(member_id="M1"):
        print(txn)

    # Demonstrating date/time usage for issue/return records, and that
    # "prevent past scheduling" style validation belongs at this layer:
    demo_due_date = date.today() + timedelta(days=14)
    print(f"\nExample due date for a 14-day loan, computed via datetime: {demo_due_date}")

    print(f"\nLog file written to: {os.path.join(DATA_DIR, 'library.log')}")
    print("Data persisted to:", path("library_data.json"))


if __name__ == "__main__":
    run_menu()
