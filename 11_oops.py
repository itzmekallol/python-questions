"""
Python Practice — Object-Oriented Programming (OOP) (40 Questions)
Solutions with explanations.

Run this file with: python python_oop_practice.py

Every problem uses classes and objects, constructors where needed, and
avoids global variables. Wherever input() would normally be used, sample
values are used instead so the script runs end-to-end without manual
entry.
"""

import random
import string
from abc import ABC, abstractmethod
from datetime import datetime

# =========================================================
# PART 1: CLASSES & OBJECTS (1-8)
# =========================================================

print("=" * 50)
print("PART 1: CLASSES & OBJECTS")
print("=" * 50)

# --- Q1: Student class ---
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

print("\nQ1:")
student1 = Student("Kallol", 20)
student1.display()

# --- Q2: Car class ---
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

print("\nQ2:")
car1 = Car("Toyota", "Corolla", 2023)
car1.display()

# --- Q3: Book class ---
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"'{self.title}' by {self.author} - ₹{self.price}")

print("\nQ3:")
book1 = Book("The Alchemist", "Paulo Coelho", 399)
book1.display()

# --- Q4: Rectangle class with area and perimeter ---
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

print("\nQ4:")
rect1 = Rectangle(10, 5)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

# --- Q5: Circle class with area and circumference ---
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * 3.14159 * self.radius, 2)

print("\nQ5:")
circle1 = Circle(7)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())

# --- Q6: Employee class ---
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Salary: ₹{self.salary}")

print("\nQ6:")
emp1 = Employee("Ananya", 65000)
emp1.display()

# --- Q7: Laptop class, multiple objects ---
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display(self):
        print(f"{self.brand} - {self.ram}GB RAM, {self.storage}GB Storage")

print("\nQ7:")
laptop1 = Laptop("Dell", 16, 512)
laptop2 = Laptop("Apple", 8, 256)
laptop1.display()
laptop2.display()

# --- Q8: Movie class ---
class Movie:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating

    def display(self):
        print(f"'{self.name}' directed by {self.director} - Rating: {self.rating}/10")

print("\nQ8:")
movie1 = Movie("Inception", "Christopher Nolan", 8.8)
movie1.display()


# =========================================================
# PART 2: CONSTRUCTORS & INSTANCE METHODS (9-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: CONSTRUCTORS & INSTANCE METHODS")
print("=" * 50)

# --- Q9: BankAccount class ---
class BankAccountBasic:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Error: Insufficient balance"
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

print("\nQ9:")
account1 = BankAccountBasic(1000)
print("After deposit 500:", account1.deposit(500))
print("After withdraw 300:", account1.withdraw(300))
print("Current balance:", account1.check_balance())

# --- Q10: Temperature class ---
class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

print("\nQ10:")
temp_converter = Temperature()
print("37C to F:", temp_converter.celsius_to_fahrenheit(37))
print("98.6F to C:", round(temp_converter.fahrenheit_to_celsius(98.6), 2))

# --- Q11: Calculator class ---
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

print("\nQ11:")
calc = Calculator()
print("5 + 3 =", calc.add(5, 3))
print("5 - 3 =", calc.subtract(5, 3))
print("5 * 3 =", calc.multiply(5, 3))
print("5 / 0 =", calc.divide(5, 0))

# --- Q12: PasswordGenerator class ---
class PasswordGenerator:
    def generate(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(characters) for _ in range(length))

print("\nQ12:")
pwd_gen = PasswordGenerator()
random.seed(42)  # seeded for reproducible demo output
print("Generated password (length 12):", pwd_gen.generate(12))

# --- Q13: StudentResult class ---
class StudentResult:
    def __init__(self, marks):
        self.marks = marks  # list of subject marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

print("\nQ13:")
result1 = StudentResult([88, 92, 79, 85, 91])
print("Total:", result1.total())
print("Average:", result1.average())
print("Grade:", result1.grade())

# --- Q14: ShoppingCart class ---
class ShoppingCartOOP:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_cart(self):
        return self.items

    def total_items(self):
        return len(self.items)

print("\nQ14:")
cart = ShoppingCartOOP()
cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")
cart.remove_item("Mouse")
print("Cart contents:", cart.display_cart())
print("Total items:", cart.total_items())


# =========================================================
# PART 3: CLASS VARIABLES & STATIC METHODS (15-18)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: CLASS VARIABLES & STATIC METHODS")
print("=" * 50)

# --- Q15: Class variable counting Student objects ---
class StudentCounter:
    total_students = 0  # class variable shared across all instances

    def __init__(self, name):
        self.name = name
        StudentCounter.total_students += 1

print("\nQ15:")
s1 = StudentCounter("Aarav")
s2 = StudentCounter("Isha")
s3 = StudentCounter("Vikram")
print("Total students created:", StudentCounter.total_students)

# --- Q16: Static method to check even number ---
class NumberUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

print("\nQ16:")
print("8 is even:", NumberUtils.is_even(8))
print("7 is even:", NumberUtils.is_even(7))

# --- Q17: Static method to check leap year ---
class DateUtils:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("\nQ17:")
print("2028 is leap year:", DateUtils.is_leap_year(2028))
print("2027 is leap year:", DateUtils.is_leap_year(2027))

# --- Q18: Class method displaying total employees ---
class EmployeeWithCount:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        EmployeeWithCount.total_employees += 1

    @classmethod
    def display_total(cls):
        return f"Total employees created: {cls.total_employees}"

print("\nQ18:")
e1 = EmployeeWithCount("Ravi")
e2 = EmployeeWithCount("Meena")
print(EmployeeWithCount.display_total())


# =========================================================
# PART 4: INHERITANCE (19-24)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: INHERITANCE")
print("=" * 50)

# --- Q19: Animal -> Dog ---
class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print(f"Dog name: {self.name}, Breed: {self.breed}")

print("\nQ19:")
dog1 = Dog("Buddy", "Labrador")
dog1.display()

# --- Q20: Vehicle -> Car with extra features ---
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class CarChild(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def display(self):
        print(f"{self.brand} - Top speed: {self.speed} km/h, Doors: {self.num_doors}")

print("\nQ20:")
car_child1 = CarChild("Honda", 180, 4)
car_child1.display()

# --- Q21: Person -> Student ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class StudentChild(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

    def display(self):
        print(f"{self.name}, Age: {self.age}, Roll No: {self.roll_number}, Course: {self.course}")

print("\nQ21:")
student_child1 = StudentChild("Diya", 19, "R101", "Computer Science")
student_child1.display()

# --- Q22: Employee -> Manager ---
class EmployeeBase:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(EmployeeBase):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"Manager {self.name}, Salary: ₹{self.salary}, Department: {self.department}")

print("\nQ22:")
manager1 = Manager("Suresh", 95000, "Engineering")
manager1.display()

# --- Q23: Shape -> Rectangle, Circle (each calculates own area) ---
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

print("\nQ23:")
shapes = [RectangleShape(4, 6), CircleShape(5)]
for shape in shapes:
    print(f"{type(shape).__name__} area:", shape.area())

# --- Q24: Multilevel inheritance: Person -> Employee -> Manager ---
class PersonBase:
    def __init__(self, name):
        self.name = name

class EmployeeMid(PersonBase):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class ManagerTop(EmployeeMid):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        print(f"Manager {self.name}, Salary: ₹{self.salary}, Team size: {self.team_size}")

print("\nQ24:")
manager2 = ManagerTop("Kavya", 110000, 8)
manager2.display()


# =========================================================
# PART 5: POLYMORPHISM (25-28)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: POLYMORPHISM")
print("=" * 50)

# --- Q25: Dog, Cat, Cow each implement sound() ---
class DogAnimal:
    def sound(self):
        return "Woof!"

class CatAnimal:
    def sound(self):
        return "Meow!"

class CowAnimal:
    def sound(self):
        return "Moo!"

print("\nQ25:")
animals = [DogAnimal(), CatAnimal(), CowAnimal()]
for animal in animals:
    print(f"{type(animal).__name__} says: {animal.sound()}")

# --- Q26: Car, Bike, Bus each implement start() ---
class CarVehicle:
    def start(self):
        return "Car starts with a key turn"

class BikeVehicle:
    def start(self):
        return "Bike starts with a kick or button"

class BusVehicle:
    def start(self):
        return "Bus starts with an ignition switch"

print("\nQ26:")
vehicles = [CarVehicle(), BikeVehicle(), BusVehicle()]
for vehicle in vehicles:
    print(f"{type(vehicle).__name__}: {vehicle.start()}")

# --- Q27: Payment system - CreditCard, DebitCard, UPI ---
class CreditCard:
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"

class DebitCard:
    def pay(self, amount):
        return f"Paid ₹{amount} using Debit Card"

class UPI:
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"

print("\nQ27:")
payment_methods = [CreditCard(), DebitCard(), UPI()]
for method in payment_methods:
    print(method.pay(1500))

# --- Q28: Notification classes - Email, SMS, Push ---
class EmailNotification:
    def send(self, message):
        return f"Sending Email: {message}"

class SMSNotification:
    def send(self, message):
        return f"Sending SMS: {message}"

class PushNotification:
    def send(self, message):
        return f"Sending Push Notification: {message}"

print("\nQ28:")
notifiers = [EmailNotification(), SMSNotification(), PushNotification()]
for notifier in notifiers:
    print(notifier.send("Your order has shipped!"))


# =========================================================
# PART 6: ENCAPSULATION (29-32)
# =========================================================

print("\n" + "=" * 50)
print("PART 6: ENCAPSULATION")
print("=" * 50)

# --- Q29: BankAccount with private balance ---
class BankAccountPrivate:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Error: Invalid or insufficient amount"
        return self.__balance

    def get_balance(self):
        return self.__balance

print("\nQ29:")
private_account = BankAccountPrivate(1000)
print("After deposit 500:", private_account.deposit(500))
print("After withdraw 2000 (should fail):", private_account.withdraw(2000))
print("Balance via getter:", private_account.get_balance())
# Direct access to __balance is not possible from outside the class as intended

# --- Q30: Employee with private salary, getter/setter ---
class EmployeePrivateSalary:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Error: Salary must be positive")

print("\nQ30:")
emp_private = EmployeePrivateSalary("Neha", 50000)
print("Initial salary:", emp_private.get_salary())
emp_private.set_salary(55000)
print("Updated salary:", emp_private.get_salary())
emp_private.set_salary(-1000)  # rejected

# --- Q31: Student with private, validated marks ---
class StudentPrivateMarks:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = None
        self.set_marks(marks)

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print(f"Error: Marks {marks} must be between 0 and 100. Marks not updated.")

    def get_marks(self):
        return self.__marks

print("\nQ31:")
student_marks = StudentPrivateMarks("Rohan", 85)
print("Initial marks:", student_marks.get_marks())
student_marks.set_marks(150)  # rejected
print("Marks after invalid attempt:", student_marks.get_marks())

# --- Q32: Product with price that can never go negative ---
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = 0
        self.set_price(price)

    def set_price(self, price):
        if price < 0:
            print(f"Error: Price cannot be negative. Keeping price at {self.__price}")
        else:
            self.__price = price

    def get_price(self):
        return self.__price

print("\nQ32:")
product1 = Product("Headphones", 1999)
print("Initial price:", product1.get_price())
product1.set_price(-500)  # rejected
print("Price after invalid attempt:", product1.get_price())


# =========================================================
# PART 7: ABSTRACTION (33-35)
# =========================================================

print("\n" + "=" * 50)
print("PART 7: ABSTRACTION")
print("=" * 50)

# --- Q33: Abstract class Shape -> Rectangle, Circle ---
class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class RectangleAbstract(AbstractShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class CircleAbstract(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * 3.14159 * self.radius, 2)

print("\nQ33:")
abstract_shapes = [RectangleAbstract(5, 3), CircleAbstract(4)]
for shape in abstract_shapes:
    print(f"{type(shape).__name__} -> Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# --- Q34: Abstract class Payment -> UPI, CreditCard, PayPal ---
class AbstractPayment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class UPIPayment(AbstractPayment):
    def process_payment(self, amount):
        return f"Processed ₹{amount} via UPI"

class CreditCardPayment(AbstractPayment):
    def process_payment(self, amount):
        return f"Processed ₹{amount} via Credit Card"

class PayPalPayment(AbstractPayment):
    def process_payment(self, amount):
        return f"Processed ₹{amount} via PayPal"

print("\nQ34:")
payment_options = [UPIPayment(), CreditCardPayment(), PayPalPayment()]
for option in payment_options:
    print(option.process_payment(2500))

# --- Q35: Abstract class Vehicle -> Car, Bike, Truck ---
class AbstractVehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class CarAbstract(AbstractVehicle):
    def start(self):
        return "Car engine started"

class BikeAbstract(AbstractVehicle):
    def start(self):
        return "Bike engine started"

class TruckAbstract(AbstractVehicle):
    def start(self):
        return "Truck engine started"

print("\nQ35:")
vehicle_options = [CarAbstract(), BikeAbstract(), TruckAbstract()]
for vehicle in vehicle_options:
    print(f"{type(vehicle).__name__}: {vehicle.start()}")


# =========================================================
# PART 8: MAGIC (DUNDER) METHODS (36-37)
# =========================================================

print("\n" + "=" * 50)
print("PART 8: MAGIC (DUNDER) METHODS")
print("=" * 50)

# --- Q36: Book class with __str__() ---
class BookWithStr:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author} - ₹{self.price}"

print("\nQ36:")
book_str = BookWithStr("Dune", "Frank Herbert", 599)
print(book_str)  # automatically uses __str__

# --- Q37: Student class with __repr__() ---
class StudentWithRepr:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __repr__(self):
        return f"StudentWithRepr(name={self.name!r}, roll_number={self.roll_number!r})"

print("\nQ37:")
student_repr = StudentWithRepr("Tanya", "R202")
print(repr(student_repr))
print(student_repr)  # falls back to __repr__ since __str__ isn't defined


# =========================================================
# PART 9: PROFESSIONAL MINI PROJECTS (38-40)
# =========================================================

print("\n" + "=" * 50)
print("PART 9: PROFESSIONAL MINI PROJECTS")
print("=" * 50)

# --- Q38: Library Management System ---
class LibraryBook:
    def __init__(self, book_id, title, author, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"[{self.book_id}] '{self.title}' by {self.author} - {self.copies} available"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, copies=1):
        if book_id in self.books:
            return f"Book ID {book_id} already exists"
        self.books[book_id] = LibraryBook(book_id, title, author, copies)
        return f"Book '{title}' added"

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_title = self.books[book_id].title
            del self.books[book_id]
            return f"Book '{removed_title}' removed"
        return "Book not found"

    def search_book(self, book_id):
        book = self.books.get(book_id)
        return str(book) if book else "Book not found"

    def display_books(self):
        return [str(book) for book in self.books.values()]

    def issue_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        if book.copies <= 0:
            return f"No copies of '{book.title}' available"
        book.copies -= 1
        return f"Issued '{book.title}'. Remaining copies: {book.copies}"

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        book.copies += 1
        return f"Returned '{book.title}'. Available copies: {book.copies}"

print("\nQ38: Library Management System")
library = Library()
print(library.add_book("B1", "The Hobbit", "J.R.R. Tolkien", 2))
print(library.add_book("B2", "1984", "George Orwell", 1))
print(library.issue_book("B2"))
print(library.issue_book("B2"))  # no copies left
print(library.return_book("B2"))
print("Search B1:", library.search_book("B1"))
print("All books:", library.display_books())
print(library.remove_book("B1"))

# --- Q39: Banking System - BankAccount, SavingsAccount, CurrentAccount ---
class BankAccountFull:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self._balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self._balance += amount
        self.transaction_history.append(f"Deposited ₹{amount}")
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            self.transaction_history.append(f"Failed withdrawal of ₹{amount} (insufficient funds)")
            return "Error: Insufficient balance"
        self._balance -= amount
        self.transaction_history.append(f"Withdrew ₹{amount}")
        return self._balance

    def transfer(self, other_account, amount):
        if amount > self._balance:
            return "Error: Insufficient balance for transfer"
        self._balance -= amount
        other_account._balance += amount
        self.transaction_history.append(f"Transferred ₹{amount} to {other_account.name}")
        other_account.transaction_history.append(f"Received ₹{amount} from {self.name}")
        return f"Transferred ₹{amount} to {other_account.name}"

    def get_balance(self):
        return self._balance

    def get_transaction_history(self):
        return self.transaction_history

class SavingsAccount(BankAccountFull):
    def __init__(self, account_number, name, balance=0, interest_rate=0.04):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self.transaction_history.append(f"Interest applied: ₹{interest:.2f}")
        return self._balance

class CurrentAccount(BankAccountFull):
    def __init__(self, account_number, name, balance=0, overdraft_limit=10000):
        super().__init__(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            return "Error: Overdraft limit exceeded"
        self._balance -= amount
        self.transaction_history.append(f"Withdrew ₹{amount}")
        return self._balance

print("\nQ39: Banking System")
savings = SavingsAccount("SAV001", "Priya", 20000, interest_rate=0.05)
current = CurrentAccount("CUR001", "Rahul", 5000, overdraft_limit=10000)

print("Savings deposit 3000:", savings.deposit(3000))
print("Savings apply interest:", round(savings.apply_interest(), 2))
print("Current withdraw 12000 (uses overdraft):", current.withdraw(12000))
print("Transfer 2000 from savings to current:", savings.transfer(current, 2000))
print("Savings balance:", round(savings.get_balance(), 2))
print("Current balance:", current.get_balance())
print("Savings transaction history:", savings.get_transaction_history())

# --- Q40: Student Management System - Student, Classroom ---
class StudentOOP:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"[{self.roll_number}] {self.name} - Marks: {self.marks}"

class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_number, name, marks):
        if roll_number in self.students:
            return f"Roll number {roll_number} already exists"
        self.students[roll_number] = StudentOOP(roll_number, name, marks)
        return f"Student {name} added"

    def remove_student(self, roll_number):
        if roll_number in self.students:
            removed_name = self.students[roll_number].name
            del self.students[roll_number]
            return f"Student {removed_name} removed"
        return "Student not found"

    def search_student(self, roll_number):
        student = self.students.get(roll_number)
        return str(student) if student else "Student not found"

    def update_student(self, roll_number, new_marks):
        if roll_number in self.students:
            self.students[roll_number].marks = new_marks
            return f"Marks updated for {self.students[roll_number].name}"
        return "Student not found"

    def display_students(self):
        return [str(student) for student in self.students.values()]

    def calculate_average_marks(self):
        if not self.students:
            return 0
        total = sum(student.marks for student in self.students.values())
        return total / len(self.students)

    def find_topper(self):
        if not self.students:
            return "No students in classroom"
        topper = max(self.students.values(), key=lambda s: s.marks)
        return str(topper)

print("\nQ40: Student Management System")
classroom = Classroom()
print(classroom.add_student("R01", "Aarav", 85))
print(classroom.add_student("R02", "Isha", 92))
print(classroom.add_student("R03", "Vikram", 78))
print(classroom.update_student("R03", 88))
print("All students:", classroom.display_students())
print("Search R02:", classroom.search_student("R02"))
print("Average marks:", round(classroom.calculate_average_marks(), 2))
print("Topper:", classroom.find_topper())
print(classroom.remove_student("R01"))
print("Remaining students:", classroom.display_students())

print("\n" + "=" * 50)
print("All 40 OOP demonstrations completed successfully.")
print("=" * 50)