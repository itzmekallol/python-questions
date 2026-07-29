"""
Python Practice — Tuples (20 Questions)
Solutions with explanations.

Run this file with: python python_tuples_practice.py
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. Feel free to
swap in input() calls when experimenting interactively.
"""

# =========================================================
# PART 1: TUPLE BASICS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: TUPLE BASICS")
print("=" * 50)

# --- Q1: Create a tuple with name, age, city ---
person = ("Kallol", 20, "Kolkata")
print("\nQ1:", person)

# --- Q2: First, last, and middle element ---
sample_tuple = (10, 20, 30, 40, 50)
print("\nQ2:")
print("First element:", sample_tuple[0])
print("Last element:", sample_tuple[-1])
print("Middle element:", sample_tuple[len(sample_tuple) // 2])

# --- Q3: Length of a tuple without len() ---
def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count

print("\nQ3: Length of sample_tuple:", tuple_length(sample_tuple))

# --- Q4: Traverse and print each element ---
print("\nQ4:")
for item in sample_tuple:
    print(item)

# --- Q5: Check whether a value exists ---
print("\nQ5: 30 in sample_tuple:", 30 in sample_tuple)
print("Q5: 99 in sample_tuple:", 99 in sample_tuple)


# =========================================================
# PART 2: TUPLE OPERATIONS (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: TUPLE OPERATIONS")
print("=" * 50)

# --- Q6: Concatenate two tuples ---
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated = tuple_a + tuple_b
print("\nQ6: Concatenated tuple:", concatenated)

# --- Q7: Repeat a tuple three times ---
repeat_demo = (1, 2)
repeated = repeat_demo * 3
print("Q7: Repeated tuple:", repeated)

# --- Q8: Count occurrences of a value ---
count_demo = (1, 2, 2, 3, 2, 4)
print("\nQ8: Count of 2:", count_demo.count(2))

# --- Q9: Index of a given element ---
print("Q9: Index of 3:", count_demo.index(3))

# --- Q10: Largest and smallest without max()/min() ---
def find_largest_smallest(t):
    largest = smallest = t[0]
    for item in t:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item
    return largest, smallest

numbers_tuple = (23, 8, 45, 12, 67, 3)
largest_val, smallest_val = find_largest_smallest(numbers_tuple)
print(f"\nQ10: Largest: {largest_val}, Smallest: {smallest_val}")


# =========================================================
# PART 3: TUPLE PACKING & UNPACKING (11-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: TUPLE PACKING & UNPACKING")
print("=" * 50)

# --- Q11: Create and unpack a tuple with three values ---
student_tuple = ("Kallol", 20, "Python")
name, age, subject = student_tuple
print("\nQ11:")
print("Name:", name)
print("Age:", age)
print("Subject:", subject)

# --- Q12: Swap two variables using tuple unpacking ---
p, q = 5, 10
print("\nQ12: Before swap ->", p, q)
p, q = q, p
print("Q12: After swap  ->", p, q)

# --- Q13: Extended unpacking ---
extended_tuple = (1, 2, 3, 4, 5, 6)
first, *middle, last = extended_tuple
print("\nQ13:")
print("First element:", first)
print("Middle elements:", middle)
print("Last element:", last)

# --- Q14: Function returning multiple values as a tuple ---
def min_max_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)

nums_for_func = (4, 8, 15, 16, 23, 42)
minimum, maximum, total = min_max_sum(nums_for_func)
print(f"\nQ14: Min: {minimum}, Max: {maximum}, Sum: {total}")


# =========================================================
# PART 4: NESTED TUPLES (15-17)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: NESTED TUPLES")
print("=" * 50)

# --- Q15: Nested tuple of student records ---
students = (
    ("Alice", 20, 88),
    ("Bob", 21, 76),
    ("Charlie", 19, 92),
)
print("\nQ15: All student records:")
for student in students:
    print(student)

# --- Q16: Student with highest marks ---
def student_with_highest_marks(records):
    top_student = records[0]
    for record in records:
        if record[2] > top_student[2]:
            top_student = record
    return top_student

print("\nQ16: Student with highest marks:", student_with_highest_marks(students))

# --- Q17: Average marks of all students ---
def average_marks(records):
    total_marks = sum(record[2] for record in records)
    return total_marks / len(records)

print("Q17: Average marks:", round(average_marks(students), 2))


# =========================================================
# PART 5: REAL-WORLD CHALLENGES (18-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: REAL-WORLD CHALLENGES")
print("=" * 50)

# --- Q18: Coordinate System ---
coordinates = ((2, 5), (8, 1), (4, 9), (6, 3))

def coordinate_analysis(coords):
    total_points = len(coords)
    largest_x_point = coords[0]
    largest_y_point = coords[0]
    for point in coords:
        if point[0] > largest_x_point[0]:
            largest_x_point = point
        if point[1] > largest_y_point[1]:
            largest_y_point = point
    return total_points, largest_x_point, largest_y_point

print("\nQ18: Coordinate System")
print("Points:", coordinates)
total_pts, max_x_point, max_y_point = coordinate_analysis(coordinates)
print("Total number of points:", total_pts)
print("Point with largest x:", max_x_point)
print("Point with largest y:", max_y_point)

# --- Q19: Product Catalog ---
products = (
    (101, "Laptop", 55000),
    (102, "Mouse", 499),
    (103, "Keyboard", 1299),
    (104, "Monitor", 8999),
)

def product_catalog_analysis(catalog):
    most_expensive = catalog[0]
    cheapest = catalog[0]
    for product in catalog:
        if product[2] > most_expensive[2]:
            most_expensive = product
        if product[2] < cheapest[2]:
            cheapest = product
    average_price = sum(product[2] for product in catalog) / len(catalog)
    return most_expensive, cheapest, average_price

print("\nQ19: Product Catalog")
print("Products:", products)
expensive_product, cheap_product, avg_price = product_catalog_analysis(products)
print("Most expensive product:", expensive_product)
print("Cheapest product:", cheap_product)
print("Average product price:", round(avg_price, 2))

# --- Q20: Employee Records ---
employees = (
    (1, "Ananya", "Engineering", 75000),
    (2, "Rohan", "Marketing", 55000),
    (3, "Priya", "Engineering", 82000),
    (4, "Vikram", "Sales", 48000),
)

def display_all_employees(records):
    for record in records:
        print(record)

def highest_paid_employee(records):
    top_earner = records[0]
    for record in records:
        if record[3] > top_earner[3]:
            top_earner = record
    return top_earner

def average_salary(records):
    return sum(record[3] for record in records) / len(records)

def search_employee_by_id(records, emp_id):
    for record in records:
        if record[0] == emp_id:
            return record
    return None

print("\nQ20: Employee Records")
print("All employees:")
display_all_employees(employees)
print("Highest-paid employee:", highest_paid_employee(employees))
print("Average salary:", round(average_salary(employees), 2))
print("Search employee ID 3:", search_employee_by_id(employees, 3))
print("Search employee ID 99:", search_employee_by_id(employees, 99))