"""
customer.py — part of the bank package.
"""


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def link_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)
