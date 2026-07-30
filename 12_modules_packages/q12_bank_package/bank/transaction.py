"""
transaction.py — part of the bank package.
"""

from datetime import datetime


class Transaction:
    def __init__(self, account_number, transaction_type, amount):
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"[{self.timestamp}] {self.transaction_type} of ₹{self.amount} "
                f"on account {self.account_number}")
