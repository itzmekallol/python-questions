"""
member.py — Member data model.
"""


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books,
        }

    @staticmethod
    def from_dict(data):
        member = Member(data["member_id"], data["name"])
        member.borrowed_books = data.get("borrowed_books", [])
        return member

    def __str__(self):
        return f"Member[{self.member_id}] {self.name} - Borrowed: {self.borrowed_books}"
