"""
Python Practice — Functional Programming (20 Questions)
Solutions with explanations.

Run this file with: python python_functional_programming_practice.py

Rules followed throughout:
- `lambda` is used wherever it fits naturally.
- `map()`, `filter()`, and `functools.reduce()` are used instead of
  explicit loops, except where a question specifically calls for a loop.
- `reduce` is imported from `functools`.
"""

from functools import reduce

# =========================================================
# PART 1: LAMBDA FUNCTIONS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: LAMBDA FUNCTIONS")
print("=" * 50)

# --- Q1: Square of a number ---
square = lambda n: n ** 2
print("\nQ1: Square of 7:", square(7))

# --- Q2: Larger of two numbers ---
larger = lambda a, b: a if a > b else b
print("Q2: Larger of 23 and 56:", larger(23, 56))

# --- Q3: Even or odd check ---
even_or_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print("Q3: 14 is", even_or_odd(14))
print("Q3: 7 is", even_or_odd(7))

# --- Q4: Convert string to uppercase ---
to_upper = lambda s: s.upper()
print("Q4: 'python' ->", to_upper("python"))

# --- Q5: Sort a list of tuples by second element ---
tuple_list = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_tuples = sorted(tuple_list, key=lambda item: item[1])
print("\nQ5: Sorted by second element:", sorted_tuples)


# =========================================================
# PART 2: map() (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: map()")
print("=" * 50)

# --- Q6: Squares of all numbers ---
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print("\nQ6: Squares:", squares)

# --- Q7: Convert strings to uppercase ---
words = ["python", "map", "filter", "reduce"]
upper_words = list(map(lambda w: w.upper(), words))
print("Q7: Uppercase words:", upper_words)

# --- Q8: Lengths of all words ---
word_lengths = list(map(len, words))
print("Q8: Word lengths:", word_lengths)

# --- Q9: Celsius to Fahrenheit conversion ---
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9 / 5) + 32, celsius_temps))
print("\nQ9: Fahrenheit temperatures:", fahrenheit_temps)

# --- Q10: Extract student names from a list of dictionaries ---
students = [
    {"name": "Aarav", "marks": 85},
    {"name": "Isha", "marks": 92},
    {"name": "Vikram", "marks": 76},
]
student_names = list(map(lambda student: student["name"], students))
print("\nQ10: Student names:", student_names)


# =========================================================
# PART 3: filter() (11-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: filter()")
print("=" * 50)

# --- Q11: Keep only even numbers ---
mixed_numbers = [3, 8, 15, 22, 7, 40, 11, 6]
even_numbers = list(filter(lambda n: n % 2 == 0, mixed_numbers))
print("\nQ11: Even numbers:", even_numbers)

# --- Q12: Keep words longer than five characters ---
word_list = ["cat", "elephant", "dog", "giraffe", "ox", "kangaroo"]
long_words = list(filter(lambda w: len(w) > 5, word_list))
print("Q12: Words longer than 5 characters:", long_words)

# --- Q13: Keep only positive numbers ---
signed_numbers = [4, -3, 7, -8, 0, -1, 9]
positive_numbers = list(filter(lambda n: n > 0, signed_numbers))
print("\nQ13: Positive numbers:", positive_numbers)

# --- Q14: Employees with salary greater than 50000 ---
employees = [
    {"name": "Ravi", "salary": 45000},
    {"name": "Meena", "salary": 62000},
    {"name": "Suresh", "salary": 78000},
    {"name": "Priya", "salary": 39000},
]
high_earners = list(filter(lambda emp: emp["salary"] > 50000, employees))
print("\nQ14: Employees earning more than ₹50,000:")
for employee in high_earners:
    print(employee)


# =========================================================
# PART 4: reduce() (15-17)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: reduce()")
print("=" * 50)

# --- Q15: Sum of all numbers ---
sum_numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda acc, n: acc + n, sum_numbers)
print("\nQ15: Sum:", total_sum)

# --- Q16: Product of all numbers ---
product_numbers = [1, 2, 3, 4, 5]
total_product = reduce(lambda acc, n: acc * n, product_numbers)
print("Q16: Product:", total_product)

# --- Q17: Longest string in a list ---
string_list = ["cat", "elephant", "dog", "giraffe", "ox"]
longest_string = reduce(lambda longest, current: current if len(current) > len(longest) else longest, string_list)
print("\nQ17: Longest string:", longest_string)


# =========================================================
# PART 5: COMBINING FUNCTIONAL TOOLS (18-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: COMBINING FUNCTIONAL TOOLS")
print("=" * 50)

# --- Q18: Filter evens, square them, sum with reduce() ---
combine_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_filtered = filter(lambda n: n % 2 == 0, combine_numbers)
squared_values = map(lambda n: n ** 2, even_filtered)
sum_of_squares = reduce(lambda acc, n: acc + n, squared_values)
print("\nQ18: Sum of squares of even numbers:", sum_of_squares)

# --- Q19: Filter students with marks >= 60, extract names, sort alphabetically ---
students_marks = [
    {"name": "Diya", "marks": 45},
    {"name": "Kabir", "marks": 78},
    {"name": "Ananya", "marks": 60},
    {"name": "Rohan", "marks": 55},
    {"name": "Meera", "marks": 92},
]
passing_students = filter(lambda s: s["marks"] >= 60, students_marks)
passing_names = map(lambda s: s["name"], passing_students)
sorted_passing_names = sorted(passing_names)
print("\nQ19: Passing student names (sorted):", sorted_passing_names)

# --- Q20: Sales Report Generator ---
products = [
    {"name": "Wireless Mouse", "category": "Electronics", "price": 499, "quantity_sold": 25},
    {"name": "Notebook", "category": "Stationery", "price": 60, "quantity_sold": 8},
    {"name": "Bluetooth Speaker", "category": "Electronics", "price": 1999, "quantity_sold": 15},
    {"name": "Desk Lamp", "category": "Home", "price": 899, "quantity_sold": 12},
    {"name": "Pen Set", "category": "Stationery", "price": 150, "quantity_sold": 5},
]

# Step 1: filter products with quantity sold > 10
popular_products = list(filter(lambda p: p["quantity_sold"] > 10, products))

# Step 2: calculate total revenue (price * quantity) for each remaining product
products_with_revenue = list(map(
    lambda p: {**p, "revenue": p["price"] * p["quantity_sold"]},
    popular_products
))

# Step 3: calculate overall revenue using reduce()
overall_revenue = reduce(lambda acc, p: acc + p["revenue"], products_with_revenue, 0)

# Step 4: sort products by revenue in descending order
sorted_by_revenue = sorted(products_with_revenue, key=lambda p: p["revenue"], reverse=True)

print("\nQ20: Sales Report Generator")
print("-" * 50)
print(f"{'Product':<20}{'Category':<15}{'Revenue':>10}")
print("-" * 50)
for product in sorted_by_revenue:
    print(f"{product['name']:<20}{product['category']:<15}{product['revenue']:>10}")
print("-" * 50)
print(f"Overall revenue (quantity sold > 10 only): ₹{overall_revenue}")