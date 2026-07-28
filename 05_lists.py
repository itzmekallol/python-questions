"""
Python Practice — Lists (50 Questions)
Solutions with explanations.

Run this file with: python python_lists_practice.py
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. Feel free to
swap in input() calls when experimenting interactively.
"""

# =========================================================
# PART 1: LIST BASICS (1-10)
# =========================================================

print("=" * 50)
print("PART 1: LIST BASICS")
print("=" * 50)

# --- Q1: Create a list of five integers ---
nums = [10, 25, 33, 47, 52]
print("\nQ1:", nums)

# --- Q2: Take five numbers as input, store in a list ---
# input_list = []
# for i in range(5):
#     input_list.append(float(input(f"Enter number {i+1}: ")))
input_list = [12, 45, 9, 67, 23]  # sample values
print("\nQ2:", input_list)

# --- Q3: First, last, and middle element ---
print("\nQ3:")
print("First element:", nums[0])
print("Last element:", nums[-1])
print("Middle element:", nums[len(nums) // 2])

# --- Q4: Length of a list without len() ---
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

print("\nQ4: Length of nums:", list_length(nums))

# --- Q5: Traverse and print every element ---
print("\nQ5:")
for item in nums:
    print(item)

# --- Q6: Traverse in reverse order ---
print("\nQ6:")
for item in reversed(nums):
    print(item)
# (equivalently: for i in range(len(nums) - 1, -1, -1): print(nums[i]))

# --- Q7: Sum of all numbers ---
def list_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total

print("\nQ7: Sum:", list_sum(nums))

# --- Q8: Average of all numbers ---
def list_average(lst):
    return list_sum(lst) / list_length(lst)

print("Q8: Average:", list_average(nums))

# --- Q9: Largest element without max() ---
def find_largest(lst):
    largest = lst[0]
    for item in lst:
        if item > largest:
            largest = item
    return largest

print("\nQ9: Largest:", find_largest(nums))

# --- Q10: Smallest element without min() ---
def find_smallest(lst):
    smallest = lst[0]
    for item in lst:
        if item < smallest:
            smallest = item
    return smallest

print("Q10: Smallest:", find_smallest(nums))


# =========================================================
# PART 2: LIST METHODS (11-18)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: LIST METHODS")
print("=" * 50)

# --- Q11: append() ---
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print("\nQ11: After append:", fruits)

# --- Q12: insert() ---
fruits.insert(1, "orange")
print("Q12: After insert at index 1:", fruits)

# --- Q13: extend() ---
more_fruits = ["grape", "kiwi"]
fruits.extend(more_fruits)
print("Q13: After extend:", fruits)

# --- Q14: remove() ---
fruits.remove("banana")
print("Q14: After remove('banana'):", fruits)

# --- Q15: pop() ---
popped_item = fruits.pop(0)
print(f"Q15: Popped '{popped_item}', remaining list:", fruits)

# --- Q16: clear() ---
temp_list = [1, 2, 3]
temp_list.clear()
print("Q16: After clear():", temp_list)

# --- Q17: index() ---
print("Q17: Index of 'cherry':", fruits.index("cherry"))

# --- Q18: count() ---
repeated_list = [1, 2, 2, 3, 2, 4]
print("Q18: Count of 2:", repeated_list.count(2))


# =========================================================
# PART 3: SEARCHING & UPDATING (19-25)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: SEARCHING & UPDATING")
print("=" * 50)

# --- Q19: Check if a value exists ---
sample_list = [5, 10, 15, 20, 25]
print("\nQ19: 15 in list:", 15 in sample_list)
print("Q19: 99 in list:", 99 in sample_list)

# --- Q20: Replace all occurrences of a value ---
def replace_value(lst, old_val, new_val):
    return [new_val if item == old_val else item for item in lst]

replace_demo = [1, 2, 3, 2, 4, 2]
print("\nQ20: Before:", replace_demo)
print("Q20: After replacing 2 with 99:", replace_value(replace_demo, 2, 99))

# --- Q21: Double the largest value ---
def double_largest(lst):
    largest_val = find_largest(lst)
    idx = lst.index(largest_val)
    lst[idx] = largest_val * 2
    return lst

double_demo = [4, 8, 15, 6, 3]
print("\nQ21: Before:", double_demo)
print("Q21: After doubling largest:", double_largest(double_demo))

# --- Q22: Swap first and last elements ---
def swap_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

swap_demo = [1, 2, 3, 4, 5]
print("\nQ22: Before:", swap_demo)
print("Q22: After swap:", swap_first_last(swap_demo))

# --- Q23: Reverse a list without reverse() or slicing ---
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

reverse_demo = [1, 2, 3, 4, 5]
print("\nQ23: Reversed:", reverse_list(reverse_demo))

# --- Q24: Rotate left by one position ---
def rotate_left(lst):
    if not lst:
        return lst
    return lst[1:] + [lst[0]]

print("\nQ24: [1,2,3,4] rotated left ->", rotate_left([1, 2, 3, 4]))

# --- Q25: Rotate right by one position ---
def rotate_right(lst):
    if not lst:
        return lst
    return [lst[-1]] + lst[:-1]

print("Q25: [1,2,3,4] rotated right ->", rotate_right([1, 2, 3, 4]))


# =========================================================
# PART 4: SORTING & DUPLICATES (26-32)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: SORTING & DUPLICATES")
print("=" * 50)

# --- Q26: Sort ascending without sort() (bubble sort) ---
def sort_ascending(lst):
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

unsorted_list = [5, 2, 9, 1, 7]
print("\nQ26: Ascending:", sort_ascending(unsorted_list))

# --- Q27: Sort descending without sort() ---
def sort_descending(lst):
    arr = lst.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Q27: Descending:", sort_descending(unsorted_list))

# --- Q28: Remove duplicates, preserve order ---
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

dup_list = [1, 3, 2, 3, 4, 1, 5]
print("\nQ28: Without duplicates:", remove_duplicates(dup_list))

# --- Q29: Second largest element ---
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

second_largest_demo = [10, 25, 8, 25, 30, 5]
print("\nQ29: Second largest:", second_largest(second_largest_demo))

# --- Q30: Second smallest element ---
def second_smallest(lst):
    unique_sorted = sorted(set(lst))
    return unique_sorted[1] if len(unique_sorted) > 1 else None

print("Q30: Second smallest:", second_smallest(second_largest_demo))

# --- Q31: Merge two sorted lists without sort() ---
def merge_sorted_lists(lst1, lst2):
    merged = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged

sorted1 = [1, 3, 5, 7]
sorted2 = [2, 4, 6, 8]
print("\nQ31: Merged sorted list:", merge_sorted_lists(sorted1, sorted2))

# --- Q32: Check if a list is sorted ---
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

print("\nQ32: [1,2,3,4] is sorted:", is_sorted([1, 2, 3, 4]))
print("Q32: [3,1,2] is sorted:", is_sorted([3, 1, 2]))


# =========================================================
# PART 5: LIST COMPREHENSION (33-36)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: LIST COMPREHENSION")
print("=" * 50)

# --- Q33: Squares from 1 to 20 ---
squares = [n ** 2 for n in range(1, 21)]
print("\nQ33: Squares:", squares)

# --- Q34: Even numbers from another list ---
mixed_numbers = [3, 8, 15, 22, 7, 40, 11, 6]
even_numbers = [n for n in mixed_numbers if n % 2 == 0]
print("\nQ34: Even numbers:", even_numbers)

# --- Q35: Convert strings to uppercase ---
lower_words = ["python", "list", "comprehension"]
upper_words = [word.upper() for word in lower_words]
print("\nQ35: Uppercase words:", upper_words)

# --- Q36: Length of each word in a sentence ---
sentence36 = "Python list comprehension is elegant"
word_lengths = [len(word) for word in sentence36.split()]
print("\nQ36: Word lengths:", word_lengths)


# =========================================================
# PART 6: NESTED LISTS (37-40)
# =========================================================

print("\n" + "=" * 50)
print("PART 6: NESTED LISTS")
print("=" * 50)

# --- Q37: 3x3 matrix ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nQ37: Matrix:")
for row in matrix:
    print(row)

# --- Q38: Sum of each row ---
print("\nQ38: Row sums:")
for row in matrix:
    print(sum(row))

# --- Q39: Sum of each column ---
print("\nQ39: Column sums:")
num_cols = len(matrix[0])
for col in range(num_cols):
    col_sum = 0
    for row in matrix:
        col_sum += row[col]
    print(col_sum)

# --- Q40: Largest element in a matrix ---
def largest_in_matrix(mat):
    largest_val = mat[0][0]
    for row in mat:
        for val in row:
            if val > largest_val:
                largest_val = val
    return largest_val

print("\nQ40: Largest in matrix:", largest_in_matrix(matrix))


# =========================================================
# PART 7: COMMON LIST PROBLEMS (41-45)
# =========================================================

print("\n" + "=" * 50)
print("PART 7: COMMON LIST PROBLEMS")
print("=" * 50)

# --- Q41: Count even and odd numbers ---
def count_even_odd(lst):
    evens = sum(1 for n in lst if n % 2 == 0)
    odds = len(lst) - evens
    return evens, odds

count_demo = [1, 2, 3, 4, 5, 6, 7, 8]
evens_count, odds_count = count_even_odd(count_demo)
print(f"\nQ41: Evens: {evens_count}, Odds: {odds_count}")

# --- Q42: Separate positives and negatives ---
def separate_signs(lst):
    positives = [n for n in lst if n >= 0]
    negatives = [n for n in lst if n < 0]
    return positives, negatives

signs_demo = [4, -3, 7, -8, 0, -1, 9]
pos, neg = separate_signs(signs_demo)
print(f"\nQ42: Positives: {pos}, Negatives: {neg}")

# --- Q43: Find all prime numbers in a list ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_demo = [2, 4, 7, 9, 11, 15, 17, 20, 23]
prime_numbers = [n for n in primes_demo if is_prime(n)]
print("\nQ43: Prime numbers:", prime_numbers)

# --- Q44: Frequency of every element ---
def element_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

freq_demo = [1, 2, 2, 3, 3, 3, 4]
print("\nQ44: Frequencies:", element_frequency(freq_demo))

# --- Q45: Split a list into two equal halves ---
def split_in_half(lst):
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]

split_demo = [1, 2, 3, 4, 5, 6]
first_half, second_half = split_in_half(split_demo)
print(f"\nQ45: First half: {first_half}, Second half: {second_half}")


# =========================================================
# PART 8: REAL-WORLD CHALLENGES (46-50)
# =========================================================

print("\n" + "=" * 50)
print("PART 8: REAL-WORLD CHALLENGES")
print("=" * 50)

# --- Q46: Student Marks Management ---
def student_marks_management(marks):
    highest = find_largest(marks)
    lowest = find_smallest(marks)
    average = list_average(marks)
    passed = sum(1 for m in marks if m >= 40)
    failed = sum(1 for m in marks if m < 40)
    return {
        "Highest Mark": highest,
        "Lowest Mark": lowest,
        "Average": round(average, 2),
        "Passed Students": passed,
        "Failed Students": failed,
    }

student_marks = [78, 45, 32, 90, 15, 60, 38, 82]
print("\nQ46: Student Marks Management")
print("Marks list:", student_marks)
for key, value in student_marks_management(student_marks).items():
    print(f"{key}: {value}")

# --- Q47: Expense Tracker ---
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount):
        self.expenses.append(amount)

    def remove_expense(self, amount):
        if amount in self.expenses:
            self.expenses.remove(amount)

    def total_expenses(self):
        return sum(self.expenses)

    def highest_expense(self):
        return max(self.expenses) if self.expenses else None

    def lowest_expense(self):
        return min(self.expenses) if self.expenses else None

    def average_expense(self):
        return sum(self.expenses) / len(self.expenses) if self.expenses else 0

print("\nQ47: Expense Tracker")
tracker = ExpenseTracker()
for exp in [250, 500, 120, 75, 400]:
    tracker.add_expense(exp)
print("Expenses:", tracker.expenses)
tracker.remove_expense(120)
print("After removing 120:", tracker.expenses)
print("Total:", tracker.total_expenses())
print("Highest:", tracker.highest_expense())
print("Lowest:", tracker.lowest_expense())
print("Average:", round(tracker.average_expense(), 2))

# --- Q48: Shopping Cart ---
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def search_product(self, product):
        return product in self.products

    def display_products(self):
        return self.products

    def total_products(self):
        return len(self.products)

print("\nQ48: Shopping Cart")
cart = ShoppingCart()
for item in ["Laptop", "Mouse", "Keyboard", "Monitor"]:
    cart.add_product(item)
print("All products:", cart.display_products())
cart.remove_product("Mouse")
print("After removing 'Mouse':", cart.display_products())
print("Search 'Keyboard':", cart.search_product("Keyboard"))
print("Total products:", cart.total_products())

# --- Q49: Number Analyzer ---
def number_analyzer(numbers):
    largest_num = find_largest(numbers)
    smallest_num = find_smallest(numbers)
    total = list_sum(numbers)
    average = total / list_length(numbers)
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]
    primes = [n for n in numbers if is_prime(n)]

    seen = set()
    duplicates = set()
    for n in numbers:
        if n in seen:
            duplicates.add(n)
        seen.add(n)

    return {
        "Largest": largest_num,
        "Smallest": smallest_num,
        "Sum": total,
        "Average": round(average, 2),
        "Even numbers": evens,
        "Odd numbers": odds,
        "Prime numbers": primes,
        "Duplicate values": list(duplicates),
    }

analyzer_demo = [4, 7, 7, 12, 15, 2, 9, 12, 17]
print("\nQ49: Number Analyzer")
print("Numbers:", analyzer_demo)
for key, value in number_analyzer(analyzer_demo).items():
    print(f"{key}: {value}")

# --- Q50: Library Book Manager ---
class LibraryBookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)

    def search_book(self, title):
        return title in self.books

    def display_books(self):
        return self.books

    def sort_books(self):
        return sorted(self.books)

    def total_books(self):
        return len(self.books)

    def book_exists(self, title):
        return title in self.books

print("\nQ50: Library Book Manager")
library = LibraryBookManager()
for book in ["The Hobbit", "1984", "Brave New World", "Animal Farm"]:
    library.add_book(book)
print("All books:", library.display_books())
library.remove_book("1984")
print("After removing '1984':", library.display_books())
print("Search 'Animal Farm':", library.search_book("Animal Farm"))
print("Sorted books:", library.sort_books())
print("Total books:", library.total_books())
print("'The Hobbit' exists:", library.book_exists("The Hobbit"))