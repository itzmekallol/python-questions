"""
Python Practice — Basics (30 Questions)
Solutions with explanations.

Run this file with: python python_basics_practice.py
Each part is separated so you can comment/uncomment sections as needed.
Wherever input() is used, sample fallback values are shown in comments.
"""

# =========================================================
# PART 1: VARIABLES & DATA TYPES (1-8)
# =========================================================

print("=" * 50)
print("PART 1: VARIABLES & DATA TYPES")
print("=" * 50)

# --- Q1: Basic variables ---
name = "Kallol"
age = 20
height = 5.9
is_student = True

print("\nQ1:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# --- Q2: One variable per data type ---
my_int = 10
my_float = 3.14
my_str = "Hello"
my_bool = True
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}

print("\nQ2:")
print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_str, type(my_str))
print(my_bool, type(my_bool))
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))
print(my_dict, type(my_dict))

# --- Q3: Swap without a third variable ---
a, b = 5, 10
print("\nQ3: Before swap ->", a, b)
a, b = b, a  # Python tuple unpacking does the swap
print("Q3: After swap  ->", a, b)

# --- Q4: Greet user by name ---
# user_name = input("Enter your name: ")
user_name = "Kallol"  # sample value (replace with input() when running interactively)
print(f"\nQ4: Hello, {user_name}!")

# --- Q5: Arithmetic on two input integers ---
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
num1, num2 = 15, 4  # sample values
print("\nQ5:")
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)

# --- Q6: Data type of a float input ---
# num = float(input("Enter a floating point number: "))
num = 3.14  # sample value
print("\nQ6:", num, "->", type(num))

# --- Q7: Type conversions ---
i_val = 10
f_val = 3.99
print("\nQ7:")
print("int to float:", float(i_val), type(float(i_val)))
print("float to int:", int(f_val), type(int(f_val)))
print("int to str:", str(i_val), type(str(i_val)))
print("str to int:", int("25"), type(int("25")))

# --- Q8: Multiple inputs in one line ---
# name_in, age_in, city_in = input("Enter name, age, city separated by space: ").split()
name_in, age_in, city_in = "Kallol", "20", "Kolkata"  # sample values
print(f"\nQ8: {name_in} is {age_in} years old and lives in {city_in}.")


# =========================================================
# PART 2: INPUT & OUTPUT (9-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: INPUT & OUTPUT")
print("=" * 50)

# --- Q9: Full name ---
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
first_name, last_name = "Kallol", "Roy"  # sample values
print("\nQ9: Full name:", first_name + " " + last_name)

# --- Q10: Age from birth year ---
# birth_year = int(input("Enter your birth year: "))
birth_year = 2004  # sample value
current_year = 2026
calculated_age = current_year - birth_year
print("\nQ10: Your age is approximately:", calculated_age)

# --- Q11: Circle area & circumference ---
# radius = float(input("Enter radius: "))
radius = 7.0  # sample value
pi_val = 3.14159
circle_area = pi_val * radius ** 2
circumference = 2 * pi_val * radius
print("\nQ11:")
print("Area:", round(circle_area, 2))
print("Circumference:", round(circumference, 2))

# --- Q12: Rectangle area & perimeter ---
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
length, width = 10.0, 5.0  # sample values
rect_area = length * width
perimeter = 2 * (length + width)
print("\nQ12:")
print("Area:", rect_area)
print("Perimeter:", perimeter)

# --- Q13: Celsius to Fahrenheit ---
# celsius = float(input("Enter temperature in Celsius: "))
celsius = 37.0  # sample value
fahrenheit = (celsius * 9 / 5) + 32
print("\nQ13:", celsius, "C =", fahrenheit, "F")

# --- Q14: Five subject marks ---
# marks = []
# for i in range(5):
#     marks.append(float(input(f"Enter marks for subject {i+1}: ")))
marks = [85, 90, 78, 92, 88]  # sample values
total_marks = sum(marks)
average_marks = total_marks / len(marks)
print("\nQ14:")
print("Total:", total_marks)
print("Average:", average_marks)


# =========================================================
# PART 3: OPERATORS (15-21)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: OPERATORS")
print("=" * 50)

# --- Q15: Arithmetic operators ---
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
x, y = 20, 3  # sample values
print("\nQ15:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# --- Q16: Comparison operators ---
print("\nQ16:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# --- Q17: Logical operators ---
p, q = True, False
print("\nQ17:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# --- Q18: Assignment operators ---
val = 10
print("\nQ18:")
val += 5; print("+=", val)
val -= 3; print("-=", val)
val *= 2; print("*=", val)
val //= 4; print("//=", val)
val **= 2; print("**=", val)
val %= 5; print("%=", val)
val /= 2; print("/=", val)

# --- Q19: Membership operators ---
sentence = "Python is fun to learn"
print("\nQ19:")
print("'Python' in sentence:", "Python" in sentence)
print("'Java' not in sentence:", "Java" not in sentence)

# --- Q20: Identity operators ---
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("\nQ20:")
print("list1 is list2:", list1 is list2)      # False - different objects
print("list1 is list3:", list1 is list3)      # True - same object
print("list1 is not list2:", list1 is not list2)

# --- Q21: Complex expression with precedence ---
result = (5 + 3) * 2 - (10 / 2) ** 2 + (6 % 4)
print("\nQ21: Result of (5+3)*2 - (10/2)**2 + (6%4) =", result)


# =========================================================
# PART 4: TYPE CONVERSION & STRING FORMATTING (22-26)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: TYPE CONVERSION & STRING FORMATTING")
print("=" * 50)

# --- Q22: Age as string -> int, add 5 years ---
# age_str = input("Enter your age: ")
age_str = "20"  # sample value
age_int = int(age_str)
print("\nQ22: Age after 5 years:", age_int + 5)

# --- Q23: Total bill (concatenation, f-string, format()) ---
# price = float(input("Enter price: "))
# quantity = int(input("Enter quantity: "))
price, quantity = 150.0, 3  # sample values
bill_total = price * quantity
print("\nQ23:")
print("Concatenation: Total bill is " + str(bill_total))
print(f"f-string: Total bill is {bill_total}")
print("format(): Total bill is {}".format(bill_total))

# --- Q24: Pi rounding ---
import math
print("\nQ24:")
print("Pi (2 decimals):", round(math.pi, 2))
print("Pi (4 decimals):", round(math.pi, 4))

# --- Q25: Student info card ---
student_name = "Kallol"
student_age = 20
course = "Python"
city = "Kolkata"
print("\nQ25:")
print("===== Student Information =====")
print(f"Name   : {student_name}")
print(f"Age    : {student_age}")
print(f"Course : {course}")
print(f"City   : {city}")
print("=" * 30)

# --- Q26: Rounded, integer, absolute value ---
# decimal_num = float(input("Enter a decimal number: "))
decimal_num = -15.6789  # sample value
print("\nQ26:")
print("Rounded:", round(decimal_num))
print("Integer:", int(decimal_num))
print("Absolute:", abs(decimal_num))


# =========================================================
# PART 5: MINI CHALLENGES (27-30)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: MINI CHALLENGES")
print("=" * 50)

# --- Q27: Simple calculator ---
def simple_calculator(n1, n2, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        return n1 / n2 if n2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

# n1 = float(input("Enter first number: "))
# n2 = float(input("Enter second number: "))
# op = input("Enter operation (+, -, *, /): ")
n1, n2, op = 12, 4, "*"  # sample values
print("\nQ27: Calculator result:", simple_calculator(n1, n2, op))

# --- Q28: Currency converter (fixed rate) ---
INR_TO_USD_RATE = 83.0  # 1 USD = 83 INR (fixed sample rate)

def inr_to_usd(inr_amount):
    return inr_amount / INR_TO_USD_RATE

def usd_to_inr(usd_amount):
    return usd_amount * INR_TO_USD_RATE

# inr_amount = float(input("Enter amount in INR: "))
# usd_amount = float(input("Enter amount in USD: "))
inr_amount, usd_amount = 1000, 50  # sample values
print("\nQ28:")
print(f"{inr_amount} INR = {inr_to_usd(inr_amount):.2f} USD")
print(f"{usd_amount} USD = {usd_to_inr(usd_amount):.2f} INR")

# --- Q29: BMI calculator ---
# weight = float(input("Enter weight in kg: "))
# height_m = float(input("Enter height in m: "))
weight, height_m = 70, 1.75  # sample values
bmi = weight / (height_m ** 2)
print("\nQ29: BMI =", round(bmi, 2))

# --- Q30: Electricity bill calculator ---
# customer_name = input("Enter customer name: ")
# units_consumed = float(input("Enter units consumed: "))
# cost_per_unit = float(input("Enter cost per unit: "))
customer_name, units_consumed, cost_per_unit = "Kallol", 250, 6.5  # sample values
total_bill = units_consumed * cost_per_unit
print("\nQ30:")
print("Customer Name:", customer_name)
print("Units Consumed:", units_consumed)
print("Cost Per Unit:", cost_per_unit)
print("Total Bill Amount:", total_bill)
