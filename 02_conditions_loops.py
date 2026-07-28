"""
Python Practice — Conditions & Loops (30 Questions)
Solutions with explanations.

Run this file with: python python_conditions_loops_practice.py
Wherever input() is used, sample fallback values are shown in comments
so the script runs end-to-end without needing manual entry. Uncomment
the input() lines to try your own values.
"""

# =========================================================
# PART 1: BASIC CONDITIONS (1-10)
# =========================================================

print("=" * 50)
print("PART 1: BASIC CONDITIONS")
print("=" * 50)

# --- Q1: Positive, Negative, or Zero ---
# num = int(input("Enter an integer: "))
num = -7  # sample value
print("\nQ1:")
if num > 0:
    print(num, "is Positive")
elif num < 0:
    print(num, "is Negative")
else:
    print(num, "is Zero")

# --- Q2: Even or Odd ---
# num2 = int(input("Enter an integer: "))
num2 = 14  # sample value
print("\nQ2:")
if num2 % 2 == 0:
    print(num2, "is Even")
else:
    print(num2, "is Odd")

# --- Q3: Voting eligibility ---
# person_age = int(input("Enter your age: "))
person_age = 19  # sample value
print("\nQ3:")
if person_age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# --- Q4: Larger of two numbers ---
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
a, b = 45, 78  # sample values
print("\nQ4:")
if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal:", a)

# --- Q5: Largest of three numbers ---
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
# z = float(input("Enter third number: "))
x, y, z = 12, 87, 45  # sample values
print("\nQ5:")
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print("Largest number:", largest)
# (equivalently: largest = max(x, y, z))

# --- Q6: Leap year ---
# year = int(input("Enter a year: "))
year = 2028  # sample value
print("\nQ6:")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

# --- Q7: Vowel or Consonant (with validation) ---
# ch = input("Enter a single alphabet character: ")
ch = "e"  # sample value
print("\nQ7:")
if len(ch) == 1 and ch.isalpha():
    if ch.lower() in "aeiou":
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")
else:
    print("Invalid input: please enter a single English letter")

# --- Q8: Divisible by both 3 and 5 ---
# num8 = int(input("Enter a number: "))
num8 = 30  # sample value
print("\nQ8:")
if num8 % 3 == 0 and num8 % 5 == 0:
    print(num8, "is divisible by both 3 and 5")
else:
    print(num8, "is NOT divisible by both 3 and 5")

# --- Q9: Grade from marks (with validation) ---
# marks = float(input("Enter marks (0-100): "))
marks = 84  # sample value
print("\nQ9:")
if 0 <= marks <= 100:
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)
else:
    print("Invalid marks: must be between 0 and 100")

# --- Q10: Month name from number ---
# month_num = int(input("Enter month number (1-12): "))
month_num = 7  # sample value
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
print("\nQ10:")
if 1 <= month_num <= 12:
    print("Month:", month_names[month_num - 1])
else:
    print("Invalid month number")


# =========================================================
# PART 2: NESTED CONDITIONS (11-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: NESTED CONDITIONS")
print("=" * 50)

# --- Q11: Life stage from age ---
# age11 = int(input("Enter age: "))
age11 = 45  # sample value
print("\nQ11:")
if age11 <= 12:
    print("Child")
else:
    if age11 <= 19:
        print("Teenager")
    else:
        if age11 <= 59:
            print("Adult")
        else:
            print("Senior Citizen")

# --- Q12: Bonus eligibility ---
# salary = float(input("Enter salary: "))
# experience = float(input("Enter years of experience: "))
salary, experience = 45000, 4  # sample values
print("\nQ12:")
# Rule: employees with 3+ years experience AND salary below 50000 get a bonus,
# OR employees with 5+ years experience regardless of salary.
if experience >= 5:
    print("Eligible for bonus (senior employee)")
else:
    if experience >= 3 and salary < 50000:
        print("Eligible for bonus (experience + salary criteria met)")
    else:
        print("Not eligible for bonus")

# --- Q13: Triangle type ---
# s1 = float(input("Enter side 1: "))
# s2 = float(input("Enter side 2: "))
# s3 = float(input("Enter side 3: "))
s1, s2, s3 = 5, 5, 8  # sample values
print("\nQ13:")
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    if s1 == s2 == s3:
        print("Equilateral Triangle")
    else:
        if s1 == s2 or s2 == s3 or s1 == s3:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
else:
    print("Invalid Triangle")

# --- Q14: Character category ---
# ch14 = input("Enter a character: ")
ch14 = "$"  # sample value
print("\nQ14:")
if ch14.isalpha():
    if ch14.isupper():
        print("Uppercase Letter")
    else:
        print("Lowercase Letter")
else:
    if ch14.isdigit():
        print("Digit")
    else:
        print("Special Character")

# --- Q15: Menu-driven calculator ---
print("\nQ15: Menu-driven calculator")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Power")
# choice = int(input("Choose an operation (1-6): "))
# n1 = float(input("Enter first number: "))
# n2 = float(input("Enter second number: "))
choice, n1, n2 = 4, 20, 8  # sample values
if choice == 1:
    print("Result:", n1 + n2)
elif choice == 2:
    print("Result:", n1 - n2)
elif choice == 3:
    print("Result:", n1 * n2)
elif choice == 4:
    if n2 != 0:
        print("Result:", n1 / n2)
    else:
        print("Error: Division by zero")
elif choice == 5:
    print("Result:", n1 % n2)
elif choice == 6:
    print("Result:", n1 ** n2)
else:
    print("Invalid choice")


# =========================================================
# PART 3: FOR LOOPS (16-21)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: FOR LOOPS")
print("=" * 50)

# --- Q16: Print 1 to 100 ---
print("\nQ16: Numbers from 1 to 100")
for i in range(1, 101):
    print(i, end=" ")
print()

# --- Q17: Print 100 to 1 ---
print("\nQ17: Numbers from 100 to 1")
for i in range(100, 0, -1):
    print(i, end=" ")
print()

# --- Q18: Even numbers between 1 and 100 ---
print("\nQ18: Even numbers from 1 to 100")
for i in range(2, 101, 2):
    print(i, end=" ")
print()

# --- Q19: Odd numbers between 1 and 100 ---
print("\nQ19: Odd numbers from 1 to 100")
for i in range(1, 101, 2):
    print(i, end=" ")
print()

# --- Q20: Sum of numbers from 1 to N ---
# N = int(input("Enter N: "))
N = 50  # sample value
sum_n = 0
for i in range(1, N + 1):
    sum_n += i
print(f"\nQ20: Sum from 1 to {N} =", sum_n)
# (equivalently: sum_n = N * (N + 1) // 2)

# --- Q21: Multiplication table of a number ---
# table_num = int(input("Enter a number: "))
table_num = 7  # sample value
print(f"\nQ21: Multiplication table of {table_num}")
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")


# =========================================================
# PART 4: WHILE LOOPS (22-26)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: WHILE LOOPS")
print("=" * 50)

# --- Q22: Print 1 to N using while loop ---
# N22 = int(input("Enter N: "))
N22 = 10  # sample value
print(f"\nQ22: Numbers from 1 to {N22}")
i = 1
while i <= N22:
    print(i, end=" ")
    i += 1
print()

# --- Q23: Factorial using while loop ---
# fact_num = int(input("Enter a number: "))
fact_num = 6  # sample value
factorial = 1
counter = fact_num
while counter > 1:
    factorial *= counter
    counter -= 1
print(f"\nQ23: Factorial of {fact_num} =", factorial)

# --- Q24: Reverse digits of a number ---
# rev_num = int(input("Enter a number: "))
rev_num = 12345  # sample value
temp = rev_num
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print(f"\nQ24: Reverse of {rev_num} =", reversed_num)

# --- Q25: Count digits in an integer ---
# digit_num = int(input("Enter a number: "))
digit_num = 987654  # sample value
temp2 = abs(digit_num)
digit_count = 0
if temp2 == 0:
    digit_count = 1
while temp2 > 0:
    digit_count += 1
    temp2 //= 10
print(f"\nQ25: Number of digits in {digit_num} =", digit_count)

# --- Q26: Palindrome check using while loop ---
# pal_num = int(input("Enter a number: "))
pal_num = 12321  # sample value
temp3 = pal_num
reversed_pal = 0
while temp3 > 0:
    digit = temp3 % 10
    reversed_pal = reversed_pal * 10 + digit
    temp3 //= 10
print(f"\nQ26: {pal_num} is", "a Palindrome" if reversed_pal == pal_num else "Not a Palindrome")


# =========================================================
# PART 5: NESTED LOOPS (27-30)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: NESTED LOOPS")
print("=" * 50)

# --- Q27: Increasing star pattern ---
print("\nQ27:")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# --- Q28: Decreasing star pattern ---
print("\nQ28:")
for i in range(rows, 0, -1):
    print("*" * i)

# --- Q29: Increasing number pattern ---
print("\nQ29:")
for i in range(1, rows + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
    print(line)
# (equivalently: print("".join(str(j) for j in range(1, i + 1))))

# --- Q30: Multiplication table 1 to 10 using nested loops ---
print("\nQ30: Multiplication table (1-10)")
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
