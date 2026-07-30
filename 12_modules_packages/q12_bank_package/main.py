"""
main.py — uses the account, transaction, and customer modules together.

Q12: Demonstrates a small package where modules collaborate.

Run with: python main.py
"""

from bank.account import Account
from bank.customer import Customer
from bank.transaction import Transaction

print("Q12: Using the bank package")

customer1 = Customer("Ananya Sharma", "C001")
account1 = Account("ACC1001", balance=5000)
customer1.link_account(account1)

account1.deposit(1500)
transaction1 = Transaction(account1.account_number, "Deposit", 1500)
print(transaction1)

account1.withdraw(800)
transaction2 = Transaction(account1.account_number, "Withdrawal", 800)
print(transaction2)

print(f"{customer1.name}'s total balance across accounts:", customer1.total_balance())
