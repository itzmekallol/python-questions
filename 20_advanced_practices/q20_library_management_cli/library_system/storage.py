"""
storage.py — JSON persistence layer for the library system.

Handles reading and writing the whole library state (books, members,
transactions) to a single JSON file, with proper file/JSON error
handling.
"""

import json
import os


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return {"books": {}, "members": {}, "transactions": []}
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"books": {}, "members": {}, "transactions": []}
        except json.JSONDecodeError:
            print(f"Warning: '{self.filename}' contained invalid JSON; starting with empty data")
            return {"books": {}, "members": {}, "transactions": []}

    def save(self, data):
        try:
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving library data: {e}")
