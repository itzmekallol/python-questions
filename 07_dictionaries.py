"""
Python Practice — Dictionaries (40 Questions)
Solutions with explanations.

Run this file with: python python_dictionaries_practice.py
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. Feel free to
swap in input() calls when experimenting interactively.
"""

# =========================================================
# PART 1: DICTIONARY BASICS (1-8)
# =========================================================

print("=" * 50)
print("PART 1: DICTIONARY BASICS")
print("=" * 50)

# --- Q1: Create a dictionary with name, age, course, city ---
person = {
    "name": "Kallol",
    "age": 20,
    "course": "Python",
    "city": "Kolkata"
}
print("\nQ1:", person)

# --- Q2: Access and print each value using its key ---
print("\nQ2:")
print("Name:", person["name"])
print("Age:", person["age"])
print("Course:", person["course"])
print("City:", person["city"])

# --- Q3: Add a new key-value pair ---
person["email"] = "kallol@example.com"
print("\nQ3: After adding 'email':", person)

# --- Q4: Update an existing key's value ---
person["city"] = "Mumbai"
print("\nQ4: After updating 'city':", person)

# --- Q5: Delete a key-value pair ---
del person["email"]
print("\nQ5: After deleting 'email':", person)

# --- Q6: Check whether a key exists ---
print("\nQ6: 'course' exists:", "course" in person)
print("Q6: 'phone' exists:", "phone" in person)

# --- Q7: Count key-value pairs without len() ---
def dict_length(d):
    count = 0
    for _ in d:
        count += 1
    return count

print("\nQ7: Number of key-value pairs:", dict_length(person))

# --- Q8: Traverse and print every key with its value ---
print("\nQ8:")
for key in person:
    print(f"{key}: {person[key]}")


# =========================================================
# PART 2: DICTIONARY METHODS (9-16)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: DICTIONARY METHODS")
print("=" * 50)

# --- Q9: keys() ---
print("\nQ9: Keys:", list(person.keys()))

# --- Q10: values() ---
print("Q10: Values:", list(person.values()))

# --- Q11: items() ---
print("Q11: Items:")
for key, value in person.items():
    print(f"{key} -> {value}")

# --- Q12: get() with default value ---
print("\nQ12: get('phone', 'Not Found') ->", person.get("phone", "Not Found"))
print("Q12: get('name', 'Not Found') ->", person.get("name", "Not Found"))

# --- Q13: popitem() ---
popitem_demo = {"a": 1, "b": 2, "c": 3}
last_item = popitem_demo.popitem()
print(f"\nQ13: Popped last item {last_item}, remaining dict:", popitem_demo)

# --- Q14: pop() a specific key ---
pop_demo = {"x": 10, "y": 20, "z": 30}
popped_value = pop_demo.pop("y")
print(f"\nQ14: Popped value {popped_value}, remaining dict:", pop_demo)

# --- Q15: clear() ---
clear_demo = {"m": 1, "n": 2}
clear_demo.clear()
print("\nQ15: After clear():", clear_demo)

# --- Q16: Copy a dictionary, verify independence ---
original = {"key1": "value1", "key2": "value2"}
copied = original.copy()
copied["key1"] = "modified"
print("\nQ16:")
print("Original:", original)
print("Copied (modified):", copied)


# =========================================================
# PART 3: NESTED DICTIONARIES (17-22)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: NESTED DICTIONARIES")
print("=" * 50)

# --- Q17: Nested dictionary of three students ---
students = {
    "S001": {"name": "Alice", "age": 20, "marks": 88},
    "S002": {"name": "Bob", "age": 21, "marks": 76},
    "S003": {"name": "Charlie", "age": 19, "marks": 92},
}
print("\nQ17:", students)

# --- Q18: Print details of a specific student ---
print("\nQ18: Details of S002:", students["S002"])

# --- Q19: Update marks of one student ---
students["S002"]["marks"] = 81
print("\nQ19: After updating S002 marks:", students["S002"])

# --- Q20: Add a new student ---
students["S004"] = {"name": "Diana", "age": 22, "marks": 85}
print("\nQ20: After adding S004:", students)

# --- Q21: Delete a student ---
del students["S001"]
print("\nQ21: After deleting S001:", students)

# --- Q22: Average marks of all students ---
def average_student_marks(student_dict):
    total = sum(details["marks"] for details in student_dict.values())
    return total / len(student_dict)

print("\nQ22: Average marks:", round(average_student_marks(students), 2))


# =========================================================
# PART 4: DICTIONARY OPERATIONS (23-28)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: DICTIONARY OPERATIONS")
print("=" * 50)

# --- Q23: Merge two dictionaries ---
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("\nQ23: Merged dictionary:", merged_dict)
# (Python 3.9+ alternative: merged_dict = dict1 | dict2)

# --- Q24: Character frequency in a string ---
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

char_freq_demo = "programming"
print("\nQ24: Character frequency of 'programming':", char_frequency(char_freq_demo))

# --- Q25: Word frequency in a sentence ---
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence25 = "the quick fox jumps over the lazy fox"
print("\nQ25: Word frequency:", word_frequency(sentence25))

# --- Q26: Invert a dictionary (unique values assumed) ---
def invert_dict(d):
    return {value: key for key, value in d.items()}

original_dict = {"a": 1, "b": 2, "c": 3}
print("\nQ26: Inverted dictionary:", invert_dict(original_dict))

# --- Q27: Key associated with the highest value ---
def key_with_highest_value(d):
    return max(d, key=d.get)

scores = {"Alice": 88, "Bob": 95, "Charlie": 79}
print("\nQ27: Key with highest value:", key_with_highest_value(scores))

# --- Q28: Sort dictionary by keys and by values ---
unsorted_dict = {"banana": 3, "apple": 5, "cherry": 1}
sorted_by_keys = dict(sorted(unsorted_dict.items()))
sorted_by_values = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print("\nQ28: Sorted by keys:", sorted_by_keys)
print("Q28: Sorted by values:", sorted_by_values)


# =========================================================
# PART 5: DICTIONARY COMPREHENSION (29-32)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: DICTIONARY COMPREHENSION")
print("=" * 50)

# --- Q29: Numbers 1-10 mapped to their squares ---
squares_dict = {n: n ** 2 for n in range(1, 11)}
print("\nQ29:", squares_dict)

# --- Q30: Only even numbers from another dictionary ---
number_dict = {1: 10, 2: 25, 3: 40, 4: 55, 5: 60}
even_values_dict = {k: v for k, v in number_dict.items() if v % 2 == 0}
print("\nQ30: Original:", number_dict)
print("Q30: Even values only:", even_values_dict)

# --- Q31: Convert two lists into a dictionary ---
keys_list = ["name", "age", "city"]
values_list = ["Kallol", 20, "Kolkata"]
combined_dict = dict(zip(keys_list, values_list))
print("\nQ31: Combined dictionary:", combined_dict)

# --- Q32: Items with values greater than 50 ---
price_dict = {"item1": 45, "item2": 78, "item3": 30, "item4": 92}
above_50 = {k: v for k, v in price_dict.items() if v > 50}
print("\nQ32: Items with value > 50:", above_50)


# =========================================================
# PART 6: REAL-WORLD CHALLENGES (33-40)
# =========================================================

print("\n" + "=" * 50)
print("PART 6: REAL-WORLD CHALLENGES")
print("=" * 50)

# --- Q33: Student Management System ---
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_no, name, age, marks):
        self.students[roll_no] = {"name": name, "age": age, "marks": marks}

    def update_student(self, roll_no, **updates):
        if roll_no in self.students:
            self.students[roll_no].update(updates)

    def delete_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]

    def search_student(self, roll_no):
        return self.students.get(roll_no, "Student not found")

    def display_all(self):
        return self.students

print("\nQ33: Student Management System")
sms = StudentManagementSystem()
sms.add_student("R01", "Aarav", 20, 85)
sms.add_student("R02", "Isha", 21, 90)
sms.update_student("R01", marks=88)
print("All students:", sms.display_all())
print("Search R02:", sms.search_student("R02"))
sms.delete_student("R01")
print("After deleting R01:", sms.display_all())

# --- Q34: Contact Book ---
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def display_all(self):
        return self.contacts

print("\nQ34: Contact Book")
book = ContactBook()
book.add_contact("Ravi", "9876543210")
book.add_contact("Meena", "9123456780")
book.update_contact("Ravi", "9999999999")
print("All contacts:", book.display_all())
print("Search 'Meena':", book.search_contact("Meena"))
book.delete_contact("Ravi")
print("After deleting 'Ravi':", book.display_all())

# --- Q35: Inventory Management ---
class InventoryManagement:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, quantity):
        self.products[product_id] = {"name": name, "price": price, "quantity": quantity}

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id]["quantity"] = quantity

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def search_product(self, product_id):
        return self.products.get(product_id, "Product not found")

    def total_inventory_value(self):
        return sum(p["price"] * p["quantity"] for p in self.products.values())

print("\nQ35: Inventory Management")
inventory = InventoryManagement()
inventory.add_product("P1", "Laptop", 55000, 5)
inventory.add_product("P2", "Mouse", 499, 20)
inventory.update_stock("P2", 15)
print("Search P1:", inventory.search_product("P1"))
print("Total inventory value:", inventory.total_inventory_value())
inventory.delete_product("P1")
print("After removing P1, total value:", inventory.total_inventory_value())

# --- Q36: Bank Account Manager ---
class BankAccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, balance=0):
        self.accounts[acc_no] = {"name": name, "balance": balance}

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]["balance"] += amount

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            if self.accounts[acc_no]["balance"] >= amount:
                self.accounts[acc_no]["balance"] -= amount
            else:
                print(f"Insufficient balance for account {acc_no}")

    def check_balance(self, acc_no):
        return self.accounts.get(acc_no, {}).get("balance", "Account not found")

    def display_all(self):
        return self.accounts

print("\nQ36: Bank Account Manager")
bank = BankAccountManager()
bank.create_account("A001", "Neha", 5000)
bank.create_account("A002", "Arjun", 2000)
bank.deposit("A001", 1500)
bank.withdraw("A002", 500)
print("Balance A001:", bank.check_balance("A001"))
print("Balance A002:", bank.check_balance("A002"))
print("All accounts:", bank.display_all())

# --- Q37: Word Frequency Analyzer ---
def word_frequency_analyzer(paragraph):
    freq = {}
    for word in paragraph.lower().split():
        cleaned_word = word.strip(".,!?;:")
        freq[cleaned_word] = freq.get(cleaned_word, 0) + 1
    most_frequent = max(freq, key=freq.get)
    least_frequent = min(freq, key=freq.get)
    return freq, most_frequent, least_frequent

paragraph37 = "Python is great. Python is easy to learn and Python is powerful."
freq_result, most_freq, least_freq = word_frequency_analyzer(paragraph37)
print("\nQ37: Word Frequency Analyzer")
print("Frequencies:", freq_result)
print("Most frequent word:", most_freq)
print("Least frequent word:", least_freq)

# --- Q38: Shopping Cart (name -> quantity) ---
class ShoppingCartDict:
    def __init__(self):
        self.cart = {}

    def add_item(self, product, quantity):
        self.cart[product] = self.cart.get(product, 0) + quantity

    def remove_item(self, product):
        if product in self.cart:
            del self.cart[product]

    def update_quantity(self, product, quantity):
        if product in self.cart:
            self.cart[product] = quantity

    def display_cart(self):
        return self.cart

    def total_items(self):
        return sum(self.cart.values())

print("\nQ38: Shopping Cart")
shopping_cart = ShoppingCartDict()
shopping_cart.add_item("Apples", 4)
shopping_cart.add_item("Bread", 2)
shopping_cart.update_quantity("Apples", 6)
print("Cart:", shopping_cart.display_cart())
print("Total items:", shopping_cart.total_items())
shopping_cart.remove_item("Bread")
print("After removing 'Bread':", shopping_cart.display_cart())

# --- Q39: Employee Database ---
class EmployeeDatabase:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, department, salary):
        self.employees[emp_id] = {"name": name, "department": department, "salary": salary}

    def update_salary(self, emp_id, new_salary):
        if emp_id in self.employees:
            self.employees[emp_id]["salary"] = new_salary

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]

    def search_employee(self, emp_id):
        return self.employees.get(emp_id, "Employee not found")

    def highest_paid_employee(self):
        return max(self.employees.items(), key=lambda item: item[1]["salary"])

    def average_salary(self):
        salaries = [emp["salary"] for emp in self.employees.values()]
        return sum(salaries) / len(salaries) if salaries else 0

print("\nQ39: Employee Database")
emp_db = EmployeeDatabase()
emp_db.add_employee("E1", "Ananya", "Engineering", 75000)
emp_db.add_employee("E2", "Rohan", "Marketing", 55000)
emp_db.add_employee("E3", "Priya", "Engineering", 82000)
emp_db.update_salary("E2", 60000)
print("Search E3:", emp_db.search_employee("E3"))
print("Highest-paid employee:", emp_db.highest_paid_employee())
print("Average salary:", round(emp_db.average_salary(), 2))
emp_db.remove_employee("E1")
print("After removing E1, average salary:", round(emp_db.average_salary(), 2))

# --- Q40: Library Management ---
class LibraryManagement:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, copies):
        self.books[book_id] = {"title": title, "author": author, "available_copies": copies}

    def issue_book(self, book_id):
        if book_id in self.books and self.books[book_id]["available_copies"] > 0:
            self.books[book_id]["available_copies"] -= 1
            return f"Book '{self.books[book_id]['title']}' issued successfully"
        return "Book not available"

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id]["available_copies"] += 1
            return f"Book '{self.books[book_id]['title']}' returned successfully"
        return "Invalid book ID"

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

    def search_book(self, book_id):
        return self.books.get(book_id, "Book not found")

    def display_all(self):
        return self.books

print("\nQ40: Library Management")
library = LibraryManagement()
library.add_book("B1", "The Hobbit", "J.R.R. Tolkien", 3)
library.add_book("B2", "1984", "George Orwell", 2)
print(library.issue_book("B1"))
print(library.issue_book("B2"))
print(library.return_book("B1"))
print("Search B2:", library.search_book("B2"))
print("All books:", library.display_all())
library.remove_book("B1")
print("After removing B1:", library.display_all())