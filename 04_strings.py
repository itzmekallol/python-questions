"""
Python Practice — Strings (30 Questions)
Solutions with explanations.

Run this file with: python python_strings_practice.py
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. Feel free to
swap in input() calls when experimenting interactively.
"""

# =========================================================
# PART 1: STRING BASICS (1-8)
# =========================================================

print("=" * 50)
print("PART 1: STRING BASICS")
print("=" * 50)

# --- Q1: Original string and its length ---
# text = input("Enter a string: ")
text = "Python Programming"  # sample value
print("\nQ1:")
print("Original string:", text)
print("Length:", len(text))

# --- Q2: First and last character ---
print("\nQ2:")
print("First character:", text[0])
print("Last character:", text[-1])

# --- Q3: Every character on a new line ---
print("\nQ3:")
for char in text:
    print(char)

# --- Q4: Reverse a string without slicing ---
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print("\nQ4: Reversed string:", reverse_string(text))

# --- Q5: Count vowels ---
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print("\nQ5: Vowel count:", count_vowels(text))

# --- Q6: Count consonants ---
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

print("Q6: Consonant count:", count_consonants(text))

# --- Q7: Count digits, alphabets, special characters ---
def categorize_characters(s):
    digits = alphabets = specials = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alphabets += 1
        elif not char.isspace():
            specials += 1
    return digits, alphabets, specials

sample7 = "Hello World 123!"
d, al, sp = categorize_characters(sample7)
print(f"\nQ7: For '{sample7}' -> Digits: {d}, Alphabets: {al}, Special characters: {sp}")

# --- Q8: Empty or whitespace-only string check ---
def is_blank(s):
    return len(s) == 0 or s.isspace()

print("\nQ8:")
print("'' is blank:", is_blank(""))
print("'   ' is blank:", is_blank("   "))
print("'hi' is blank:", is_blank("hi"))


# =========================================================
# PART 2: STRING METHODS (9-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: STRING METHODS")
print("=" * 50)

sample9 = "python programming language"
print("\nQ9: Original ->", sample9)
print("Uppercase:", sample9.upper())
print("Lowercase:", sample9.lower())
print("Title Case:", sample9.title())
print("Capitalized:", sample9.capitalize())

# --- Q10: Strip leading/trailing spaces ---
sample10 = "   Hello Python   "
print("\nQ10:")
print(f"Before: '{sample10}'")
print(f"After : '{sample10.strip()}'")

# --- Q11: Replace all occurrences of a word ---
sample11 = "I like cats. Cats are great pets."
print("\nQ11:")
print("Before:", sample11)
print("After:", sample11.replace("Cats", "Dogs").replace("cats", "dogs"))

# --- Q12: Count occurrences of a character/word ---
sample12 = "banana"
print("\nQ12:")
print(f"'a' appears {sample12.count('a')} times in '{sample12}'")
sentence12 = "the quick fox jumps over the lazy fox"
print(f"'fox' appears {sentence12.count('fox')} times in the sentence")

# --- Q13: startswith / endswith ---
sample13 = "python_practice.py"
print("\nQ13:")
print("Starts with 'python':", sample13.startswith("python"))
print("Ends with '.py':", sample13.endswith(".py"))

# --- Q14: Split sentence into words, print each on a new line ---
sentence14 = "Learning Python is fun and rewarding"
print("\nQ14:")
words14 = sentence14.split()
for word in words14:
    print(word)

# --- Q15: Join list of words into a sentence ---
word_list = ["Python", "is", "a", "powerful", "language"]
joined_sentence = " ".join(word_list)
print("\nQ15: Joined sentence:", joined_sentence)
joined_with_dash = "-".join(word_list)
print("Joined with '-':", joined_with_dash)


# =========================================================
# PART 3: STRING SEARCHING & VALIDATION (16-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: STRING SEARCHING & VALIDATION")
print("=" * 50)

# --- Q16: Substring existence ---
paragraph = "Python makes programming enjoyable"
substring = "programming"
print("\nQ16:")
print(f"'{substring}' in text:", substring in paragraph)

# --- Q17: First and last occurrence of a character ---
sample17 = "programming"
char17 = "g"
print("\nQ17:")
print("First occurrence of 'g':", sample17.find(char17))
print("Last occurrence of 'g':", sample17.rfind(char17))

# --- Q18: Palindrome check (ignore case) ---
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print("\nQ18:")
print("'Madam' is palindrome:", is_palindrome("Madam"))
print("'Hello' is palindrome:", is_palindrome("Hello"))

# --- Q19: Anagram check ---
def is_anagram(s1, s2):
    s1_clean = sorted(s1.lower().replace(" ", ""))
    s2_clean = sorted(s2.lower().replace(" ", ""))
    return s1_clean == s2_clean

print("\nQ19:")
print("'listen' & 'silent' are anagrams:", is_anagram("listen", "silent"))
print("'hello' & 'world' are anagrams:", is_anagram("hello", "world"))

# --- Q20: Password validation ---
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    if not has_digit:
        return False, "Password must contain at least one digit"
    if not has_special:
        return False, "Password must contain at least one special character"
    return True, "Password is valid"

print("\nQ20:")
for pwd in ["weak", "StrongPass1!", "nouppercase1!", "NOLOWERCASE1!"]:
    valid, message = validate_password(pwd)
    print(f"'{pwd}' -> {message}")


# =========================================================
# PART 4: STRING FORMATTING (21-24)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: STRING FORMATTING")
print("=" * 50)

# --- Q21: Student report using f-strings ---
student_name = "Kallol"
roll_number = 21
course = "Python Programming"
student_marks = 88
student_grade = "B"

print("\nQ21:")
print(f"""
===== Student Report =====
Name       : {student_name}
Roll No.   : {roll_number}
Course     : {course}
Marks      : {student_marks}
Grade      : {student_grade}
===========================
""")

# --- Q22: Format float to 2 and 4 decimal places ---
float_num = 22 / 7
print("Q22:")
print(f"2 decimal places: {float_num:.2f}")
print(f"4 decimal places: {float_num:.4f}")

# --- Q23: Center a title within a fixed width ---
title = "PYTHON"
print("\nQ23:")
print(title.center(30, "*"))

# --- Q24: Invoice using string formatting ---
product_name = "Wireless Mouse"
quantity = 3
price = 499.50
invoice_total = quantity * price

print("\nQ24:")
print("=" * 35)
print("{:<20}{:>15}".format("Product Name:", product_name))
print("{:<20}{:>15}".format("Quantity:", quantity))
print("{:<20}{:>15}".format("Price per unit:", f"₹{price:.2f}"))
print("{:<20}{:>15}".format("Total:", f"₹{invoice_total:.2f}"))
print("=" * 35)


# =========================================================
# PART 5: ADVANCED STRING PROBLEMS (25-28)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: ADVANCED STRING PROBLEMS")
print("=" * 50)

# --- Q25: Remove duplicate characters, preserve order ---
def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

sample25 = "programming"
print("\nQ25:")
print(f"'{sample25}' without duplicates -> '{remove_duplicates(sample25)}'")

# --- Q26: Most frequent character ---
def most_frequent_char(s):
    s_clean = s.replace(" ", "")
    frequency = {}
    for char in s_clean:
        frequency[char] = frequency.get(char, 0) + 1
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent, frequency[most_frequent]

sample26 = "success rate"
char26, freq26 = most_frequent_char(sample26)
print(f"\nQ26: Most frequent character in '{sample26}' -> '{char26}' ({freq26} times)")

# --- Q27: String compression using character counts ---
def compress_string(s):
    if not s:
        return s
    compressed = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    compressed += s[-1] + str(count)
    return compressed

sample27 = "aaabbcccc"
print(f"\nQ27: Compressed '{sample27}' -> '{compress_string(sample27)}'")

# --- Q28: Longest word in a sentence ---
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        cleaned_word = word.strip(".,!?;:")
        if len(cleaned_word) > len(longest):
            longest = cleaned_word
    return longest

sentence28 = "Python programming is incredibly powerful and versatile."
print(f"\nQ28: Longest word in the sentence -> '{longest_word(sentence28)}'")


# =========================================================
# PART 6: MINI CHALLENGES (29-30)
# =========================================================

print("\n" + "=" * 50)
print("PART 6: MINI CHALLENGES")
print("=" * 50)

# --- Q29: Word Statistics Program ---
def word_statistics(text_input):
    total_chars = len(text_input)
    words = text_input.split()
    total_words = len(words)

    vowels = "aeiouAEIOU"
    total_vowels = sum(1 for c in text_input if c in vowels)
    total_consonants = sum(1 for c in text_input if c.isalpha() and c not in vowels)
    total_digits = sum(1 for c in text_input if c.isdigit())
    total_specials = sum(1 for c in text_input if not c.isalnum() and not c.isspace())

    avg_word_length = (sum(len(w.strip(".,!?;:")) for w in words) / total_words) if total_words else 0

    return {
        "Total characters": total_chars,
        "Total words": total_words,
        "Total vowels": total_vowels,
        "Total consonants": total_consonants,
        "Total digits": total_digits,
        "Total special characters": total_specials,
        "Average word length": round(avg_word_length, 2),
    }

sample29 = "Python 3 is fun, fast & powerful!"
print("\nQ29: Word Statistics for:", f"'{sample29}'")
stats = word_statistics(sample29)
for key, value in stats.items():
    print(f"{key}: {value}")

# --- Q30: Text Formatter (menu-driven) ---
def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def to_title_case(s):
    return s.title()

def reverse_text(s):
    return s[::-1]

def word_count(s):
    return len(s.split())

def remove_extra_spaces(s):
    return " ".join(s.split())

def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)

def check_palindrome_text(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def text_formatter_menu():
    menu_text = """
    ----- Text Formatter -----
    1. Convert to Uppercase
    2. Convert to Lowercase
    3. Title Case
    4. Reverse Text
    5. Count Words
    6. Remove Extra Spaces
    7. Replace Words
    8. Check Palindrome
    9. Exit
    ---------------------------
    """
    print(menu_text)

    # For real interactive use, wrap this logic in a while loop like:
    #
    # while True:
    #     choice = int(input("Enter your choice (1-9): "))
    #     if choice == 9:
    #         print("Exiting Text Formatter. Goodbye!")
    #         break
    #     text_in = input("Enter text: ")
    #     if choice == 1:
    #         print(to_uppercase(text_in))
    #     elif choice == 2:
    #         print(to_lowercase(text_in))
    #     elif choice == 3:
    #         print(to_title_case(text_in))
    #     elif choice == 4:
    #         print(reverse_text(text_in))
    #     elif choice == 5:
    #         print(word_count(text_in))
    #     elif choice == 6:
    #         print(remove_extra_spaces(text_in))
    #     elif choice == 7:
    #         old_w = input("Word to replace: ")
    #         new_w = input("Replace with: ")
    #         print(replace_word(text_in, old_w, new_w))
    #     elif choice == 8:
    #         print("Palindrome" if check_palindrome_text(text_in) else "Not a Palindrome")
    #     else:
    #         print("Invalid choice, try again.")

    demo_text = "  Python   is   Fun  "
    demo_choices = [
        (1, "Uppercase", to_uppercase(demo_text)),
        (2, "Lowercase", to_lowercase(demo_text)),
        (3, "Title Case", to_title_case(demo_text)),
        (4, "Reverse Text", reverse_text(demo_text)),
        (5, "Word Count", word_count(demo_text)),
        (6, "Remove Extra Spaces", f"'{remove_extra_spaces(demo_text)}'"),
        (7, "Replace Words", replace_word(demo_text, "Fun", "Awesome")),
        (8, "Palindrome Check", "Palindrome" if check_palindrome_text("Madam") else "Not a Palindrome"),
    ]

    for choice, label, output in demo_choices:
        print(f"Choice {choice} ({label}) -> {output}")

    print("Choice 9 (Exit) -> Exiting Text Formatter. Goodbye!")

print("\nQ30:")
text_formatter_menu()
