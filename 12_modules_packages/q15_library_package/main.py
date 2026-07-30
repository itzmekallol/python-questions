"""
main.py — entry point for the library package.

Q15: Library Management Package.
Structure:
    library/
    ├── __init__.py
    ├── book.py
    ├── member.py
    ├── library.py
    ├── file_handler.py
    └── main.py   (this file sits alongside the package, importing from it)

Run with: python main.py
"""

from library.library import Library
from library.member import Member

print("Q15: Library Management Package")

lib = Library(data_file="library_data.txt")

print(lib.add_book("B1", "The Hobbit", "J.R.R. Tolkien"))
print(lib.add_book("B2", "1984", "George Orwell"))
print(lib.add_book("B3", "Dune", "Frank Herbert"))

member1 = Member("M001", "Priya")

print(lib.issue_book("B2", member1))
print(lib.issue_book("B2", member1))  # already issued
print("All books:", lib.display_books())
print(lib.return_book("B2", member1))
print("Search B3:", lib.search_book("B3"))
print(lib.remove_book("B1"))
print("All books after removal:", lib.display_books())
print(member1)

print("\nData saved to and loaded from:", lib.data_file)
