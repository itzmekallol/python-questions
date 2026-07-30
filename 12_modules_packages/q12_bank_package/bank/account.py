"""
account.py — part of the bank package.
"""


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Error: Insufficient balance"
        self.balance -= amount
        return self.balance
