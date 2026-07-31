"""
transaction.py — Transaction data model, representing one issue or
return event, with a real timestamp from the datetime module.
"""

from datetime import datetime


class Transaction:
    def __init__(self, member_id, book_id, action, timestamp=None):
        self.member_id = member_id
        self.book_id = book_id
        self.action = action  # "issue" or "return"
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "book_id": self.book_id,
            "action": self.action,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def from_dict(data):
        return Transaction(data["member_id"], data["book_id"], data["action"], data["timestamp"])

    def __str__(self):
        return f"[{self.timestamp}] {self.action.upper()} - Book {self.book_id} - Member {self.member_id}"
