"""
Python Practice — Sets (20 Questions)
Solutions with explanations.

Run this file with: python python_sets_practice.py
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. Feel free to
swap in input() calls when experimenting interactively.
"""

# =========================================================
# PART 1: SET BASICS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: SET BASICS")
print("=" * 50)

# --- Q1: Create a set of five unique integers ---
unique_numbers = {12, 45, 7, 89, 23}
print("\nQ1:", unique_numbers)

# --- Q2: Take 10 numbers as input, store in a set ---
# input_numbers = set()
# for i in range(10):
#     input_numbers.add(int(input(f"Enter number {i+1}: ")))
input_numbers = {5, 8, 2, 5, 9, 8, 1, 3, 5, 7}  # sample values with intentional duplicates
print("\nQ2: Set from input:", input_numbers)
print("Q2 explanation: A set automatically removes duplicate values, so even though")
print("10 numbers were entered, the set only stores each unique value once —")
print("that's why the set's size can be smaller than 10.")

# --- Q3: Add a new element ---
sample_set = {1, 2, 3}
sample_set.add(4)
print("\nQ3: After adding 4:", sample_set)

# --- Q4: Remove an element, handle missing element ---
print("\nQ4:")
sample_set.discard(2)  # discard() does not raise an error if element is missing
print("After discard(2):", sample_set)
sample_set.discard(99)  # safe even though 99 doesn't exist
print("After discard(99) [not present]:", sample_set)

# Using remove() with a try/except to handle a missing element safely
try:
    sample_set.remove(100)
except KeyError:
    print("KeyError caught: 100 is not in the set, so remove() failed safely")

# --- Q5: Check if an element exists ---
print("\nQ5: 3 in sample_set:", 3 in sample_set)
print("Q5: 50 in sample_set:", 50 in sample_set)


# =========================================================
# PART 2: SET METHODS (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: SET METHODS")
print("=" * 50)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# --- Q6: Union ---
print("\nQ6: Union:", set_a.union(set_b))

# --- Q7: Intersection ---
print("Q7: Intersection:", set_a.intersection(set_b))

# --- Q8: Difference ---
print("Q8: Difference (A - B):", set_a.difference(set_b))
print("Q8: Difference (B - A):", set_b.difference(set_a))

# --- Q9: Symmetric difference ---
print("Q9: Symmetric difference:", set_a.symmetric_difference(set_b))

# --- Q10: Clear a set ---
clear_demo_set = {10, 20, 30}
clear_demo_set.clear()
print("\nQ10: After clear():", clear_demo_set)


# =========================================================
# PART 3: SET OPERATIONS (11-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: SET OPERATIONS")
print("=" * 50)

# --- Q11: Subset check ---
subset_demo = {1, 2}
superset_demo = {1, 2, 3, 4}
print("\nQ11: {1,2} is subset of {1,2,3,4}:", subset_demo.issubset(superset_demo))

# --- Q12: Superset check ---
print("Q12: {1,2,3,4} is superset of {1,2}:", superset_demo.issuperset(subset_demo))

# --- Q13: Disjoint check ---
disjoint_a = {1, 2, 3}
disjoint_b = {4, 5, 6}
overlapping_set = {3, 4, 5}
print("\nQ13: {1,2,3} and {4,5,6} are disjoint:", disjoint_a.isdisjoint(disjoint_b))
print("Q13: {1,2,3} and {3,4,5} are disjoint:", disjoint_a.isdisjoint(overlapping_set))

# --- Q14: Remove duplicates from a list using a set ---
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = list(set(list_with_duplicates))
print("\nQ14: Original list:", list_with_duplicates)
print("Q14: Without duplicates (order not guaranteed):", unique_list)

# --- Q15: Unique words in a sentence ---
sentence15 = "the quick brown fox jumps over the lazy fox"
unique_words = set(sentence15.split())
print("\nQ15: Unique words:", unique_words)


# =========================================================
# PART 4: PRACTICAL PROBLEMS (16-18)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: PRACTICAL PROBLEMS")
print("=" * 50)

# --- Q16: Students in two classes ---
class_1_students = ["Alice", "Bob", "Charlie", "Diana"]
class_2_students = ["Charlie", "Diana", "Ethan", "Fiona"]

set_class_1 = set(class_1_students)
set_class_2 = set(class_2_students)

print("\nQ16:")
print("Enrolled in both classes:", set_class_1 & set_class_2)
print("Only in class 1:", set_class_1 - set_class_2)
print("Only in class 2:", set_class_2 - set_class_1)
print("All unique students:", set_class_1 | set_class_2)

# --- Q17: Products purchased by two customers ---
customer_1_products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
customer_2_products = ["Mouse", "Monitor", "Webcam", "Headset"]

set_customer_1 = set(customer_1_products)
set_customer_2 = set(customer_2_products)

print("\nQ17:")
print("Common products:", set_customer_1 & set_customer_2)
print("Purchased by only one customer:", set_customer_1 ^ set_customer_2)
print("All unique products:", set_customer_1 | set_customer_2)

# --- Q18: Unique words in alphabetical order ---
paragraph18 = "Python is fun. Python is powerful. Learning Python is rewarding."
cleaned_words = {word.strip(".,!?;:").lower() for word in paragraph18.split()}
print("\nQ18: Unique words (alphabetical order):", sorted(cleaned_words))


# =========================================================
# PART 5: REAL-WORLD CHALLENGES (19-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: REAL-WORLD CHALLENGES")
print("=" * 50)

# --- Q19: Website Visitor Tracker ---
class VisitorTracker:
    def __init__(self):
        self.visitors = set()

    def add_visitor(self, visitor_id):
        self.visitors.add(visitor_id)

    def remove_visitor(self, visitor_id):
        self.visitors.discard(visitor_id)

    def has_visited(self, visitor_id):
        return visitor_id in self.visitors

    def total_unique_visitors(self):
        return len(self.visitors)

    def display_all_visitors(self):
        return self.visitors

print("\nQ19: Website Visitor Tracker")
tracker = VisitorTracker()
for vid in ["V001", "V002", "V003", "V001"]:  # V001 added twice
    tracker.add_visitor(vid)
print("All visitor IDs:", tracker.display_all_visitors())
print("Total unique visitors:", tracker.total_unique_visitors())
print("Has 'V002' visited:", tracker.has_visited("V002"))
tracker.remove_visitor("V003")
print("After removing 'V003':", tracker.display_all_visitors())

# --- Q20: Course Enrollment System ---
class CourseEnrollmentSystem:
    def __init__(self):
        self.courses = {}

    def enroll_student(self, course_name, student_id):
        if course_name not in self.courses:
            self.courses[course_name] = set()
        self.courses[course_name].add(student_id)

    def students_in_both(self, course_1, course_2):
        return self.courses.get(course_1, set()) & self.courses.get(course_2, set())

    def students_in_only_one(self, course_1, course_2):
        return self.courses.get(course_1, set()) ^ self.courses.get(course_2, set())

    def all_enrolled_students(self):
        all_students = set()
        for student_set in self.courses.values():
            all_students |= student_set
        return all_students

    def is_subset(self, course_1, course_2):
        return self.courses.get(course_1, set()).issubset(self.courses.get(course_2, set()))

    def total_unique_students(self):
        return len(self.all_enrolled_students())

print("\nQ20: Course Enrollment System")
enrollment = CourseEnrollmentSystem()
for sid in ["S1", "S2", "S3", "S4"]:
    enrollment.enroll_student("Python101", sid)
for sid in ["S3", "S4", "S5", "S6"]:
    enrollment.enroll_student("DataScience101", sid)

print("Students in both courses:", enrollment.students_in_both("Python101", "DataScience101"))
print("Students in only one course:", enrollment.students_in_only_one("Python101", "DataScience101"))
print("All enrolled students:", enrollment.all_enrolled_students())
print("Python101 students subset of DataScience101:",
      enrollment.is_subset("Python101", "DataScience101"))
print("Total unique students:", enrollment.total_unique_students())