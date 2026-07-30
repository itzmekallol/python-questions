"""
Python Practice — Regular Expressions (20 Questions)
Solutions with explanations.

Run this file with: python python_regex_practice.py

Rules followed throughout:
- Only Python's built-in `re` module is used.
- Every problem is solved with a regex, not manual string scanning.
- Solutions are written as small, reusable functions.

Q19's Log File Analyzer reads a real sample log file created inside a
"practice_files" folder next to this script.
"""

import re
import os
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: REGEX BASICS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: REGEX BASICS")
print("=" * 50)

# --- Q1: Check whether a string contains at least one digit ---
def has_digit(text):
    return bool(re.search(r"\d", text))

print("\nQ1:")
print("'abc123' has digit:", has_digit("abc123"))
print("'abcdef' has digit:", has_digit("abcdef"))

# --- Q2: Count how many digits are present in a string ---
def count_digits(text):
    return len(re.findall(r"\d", text))

print("\nQ2: Digit count in 'Room 42, Floor 3B':", count_digits("Room 42, Floor 3B"))

# --- Q3: Find all words in a sentence ---
def find_words(text):
    return re.findall(r"\b\w+\b", text)

print("\nQ3:", find_words("Regular expressions are powerful tools!"))

# --- Q4: Extract all numbers from a string ---
def extract_numbers(text):
    return re.findall(r"\d+", text)

sample4 = "Order123 costs 450 rupees and discount is 20%"
print("\nQ4:", extract_numbers(sample4))

# --- Q5: Check whether a string starts with one word and ends with another ---
def starts_and_ends_with(text, start_word, end_word):
    pattern = rf"^{re.escape(start_word)}\b.*\b{re.escape(end_word)}$"
    return bool(re.match(pattern, text))

print("\nQ5:")
print(starts_and_ends_with("Python is fun to learn", "Python", "learn"))
print(starts_and_ends_with("Python is fun to learn", "Java", "learn"))


# =========================================================
# PART 2: CHARACTER CLASSES & QUANTIFIERS (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: CHARACTER CLASSES & QUANTIFIERS")
print("=" * 50)

# --- Q6: Only alphabets ---
def is_only_alphabets(text):
    return bool(re.fullmatch(r"[A-Za-z]+", text))

print("\nQ6:")
print("'HelloWorld' only alphabets:", is_only_alphabets("HelloWorld"))
print("'Hello World' only alphabets:", is_only_alphabets("Hello World"))

# --- Q7: Only lowercase letters ---
def is_only_lowercase(text):
    return bool(re.fullmatch(r"[a-z]+", text))

print("\nQ7:")
print("'python' only lowercase:", is_only_lowercase("python"))
print("'Python' only lowercase:", is_only_lowercase("Python"))

# --- Q8: Only uppercase letters ---
def is_only_uppercase(text):
    return bool(re.fullmatch(r"[A-Z]+", text))

print("\nQ8:")
print("'PYTHON' only uppercase:", is_only_uppercase("PYTHON"))
print("'Python' only uppercase:", is_only_uppercase("Python"))

# --- Q9: Words having exactly 5 letters ---
def find_five_letter_words(text):
    return re.findall(r"\b[A-Za-z]{5}\b", text)

print("\nQ9:", find_five_letter_words("Snake plays magic tricks every night"))

# --- Q10: Words containing at least one vowel ---
def find_words_with_vowel(text):
    words = re.findall(r"\b\w+\b", text)
    return [word for word in words if re.search(r"[aeiouAEIOU]", word)]

print("\nQ10:", find_words_with_vowel("Sky fly try python rhythm code"))


# =========================================================
# PART 3: VALIDATION PROBLEMS (11-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: VALIDATION PROBLEMS")
print("=" * 50)

# --- Q11: Validate an email address ---
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.fullmatch(pattern, email))

print("\nQ11:")
for test_email in ["user@example.com", "bad-email", "user.name@sub.domain.co.in"]:
    print(f"'{test_email}' ->", is_valid_email(test_email))

# --- Q12: Validate an Indian mobile number ---
def is_valid_indian_mobile(number):
    pattern = r"^[6789]\d{9}$"
    return bool(re.fullmatch(pattern, number))

print("\nQ12:")
for test_number in ["9876543210", "12345678", "5123456789"]:
    print(f"'{test_number}' ->", is_valid_indian_mobile(test_number))

# --- Q13: Validate a password ---
def is_valid_password(password):
    has_min_length = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))
    return all([has_min_length, has_upper, has_lower, has_digit, has_special])

print("\nQ13:")
for test_password in ["weak", "StrongPass1!", "nouppercase1!"]:
    print(f"'{test_password}' ->", is_valid_password(test_password))

# --- Q14: Validate DD-MM-YYYY format (format only, not calendar correctness) ---
def is_valid_date_format(date_string):
    pattern = r"^\d{2}-\d{2}-\d{4}$"
    return bool(re.fullmatch(pattern, date_string))

print("\nQ14:")
for test_date in ["29-07-2026", "2026-07-29", "5-7-2026", "99-99-9999"]:
    print(f"'{test_date}' ->", is_valid_date_format(test_date))
    # note: "99-99-9999" passes the FORMAT check even though it's not a real
    # calendar date - the question asks for format validation only

# --- Q15: Validate a URL ---
def is_valid_url(url):
    pattern = r"^https?://(www\.)?[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+(/\S*)?$"
    return bool(re.fullmatch(pattern, url))

print("\nQ15:")
for test_url in ["https://example.com", "http://example.org", "https://www.example.in", "not a url"]:
    print(f"'{test_url}' ->", is_valid_url(test_url))


# =========================================================
# PART 4: SEARCH & REPLACE (16-18)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: SEARCH & REPLACE")
print("=" * 50)

# --- Q16: Replace all digits with * ---
def mask_digits(text):
    return re.sub(r"\d", "*", text)

print("\nQ16:", mask_digits("Phone: 9876543210"))

# --- Q17: Remove all special characters, keep letters/digits/spaces ---
def remove_special_characters(text):
    return re.sub(r"[^A-Za-z0-9\s]", "", text)

print("\nQ17:", remove_special_characters("Hello!! World@@ #2026 $$$"))

# --- Q18: Extract all hashtags from a post ---
def extract_hashtags(text):
    return re.findall(r"#(\w+)", text)

sample18 = "Learning #Python and #Regex is fun! #Coding"
print("\nQ18:", extract_hashtags(sample18))


# =========================================================
# PART 5: REAL-WORLD MINI PROJECTS (19-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q19: Log File Analyzer ---
sample_log_content = """\
192.168.1.10 - - [29/Jul/2026:09:00:01] "GET /index.html HTTP/1.1" 200
192.168.1.15 - - [29/Jul/2026:09:01:22] "GET /about.html HTTP/1.1" 200
10.0.0.5 - - [29/Jul/2026:09:02:47] "POST /login HTTP/1.1" 401
192.168.1.10 - - [29/Jul/2026:09:03:10] "GET /dashboard HTTP/1.1" 200
172.16.0.3 - - [29/Jul/2026:09:04:35] "GET /missing-page HTTP/1.1" 404
10.0.0.5 - - [29/Jul/2026:09:05:59] "POST /login HTTP/1.1" 200
192.168.1.15 - - [29/Jul/2026:09:06:12] "GET /api/data HTTP/1.1" 500
"""

with open(path("server.log"), "w") as f:
    f.write(sample_log_content)

def analyze_log_file(filename):
    with open(filename, "r") as f:
        log_text = f.read()

    ip_addresses = re.findall(r"^(\d{1,3}(?:\.\d{1,3}){3})", log_text, re.MULTILINE)
    dates = re.findall(r"\[(\d{2}/\w{3}/\d{4}):", log_text)
    times = re.findall(r":(\d{2}:\d{2}:\d{2})\]", log_text)
    status_codes = re.findall(r'"\s(\d{3})', log_text)
    urls = re.findall(r'"[A-Z]+\s(\S+)\sHTTP', log_text)

    return {
        "ip_addresses": ip_addresses,
        "dates": dates,
        "times": times,
        "status_codes": status_codes,
        "urls": urls,
    }

print("\nQ19: Log File Analyzer")
log_data = analyze_log_file(path("server.log"))
print("IP addresses:", log_data["ip_addresses"])
print("Dates:", log_data["dates"])
print("Times:", log_data["times"])
print("Status codes:", log_data["status_codes"])
print("Requested URLs:", log_data["urls"])

status_frequency = Counter(log_data["status_codes"])
print("\nStatus code frequency summary:")
for status_code, frequency in sorted(status_frequency.items()):
    print(f"{status_code}: {frequency}")

# --- Q20: User Registration Validator ---
def validate_username(username):
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{3,19}", username))

def validate_registration(username, password, email, phone):
    errors = []

    if not validate_username(username):
        errors.append(
            "Username must start with a letter, be 4-20 characters, "
            "and contain only letters, digits, or underscores."
        )
    if not is_valid_password(password):
        errors.append(
            "Password must be at least 8 characters and include an uppercase "
            "letter, a lowercase letter, a digit, and a special character."
        )
    if not is_valid_email(email):
        errors.append("Email address format is invalid.")
    if not is_valid_indian_mobile(phone):
        errors.append("Phone number must be a 10-digit number starting with 6, 7, 8, or 9.")

    if errors:
        return False, errors
    return True, ["Registration successful!"]

print("\nQ20: User Registration Validator")

print("\n-- Valid registration --")
success, messages = validate_registration("kallol_20", "StrongPass1!", "kallol@example.com", "9876543210")
print("Success:", success)
for message in messages:
    print("-", message)

print("\n-- Invalid registration --")
success, messages = validate_registration("k1", "weak", "not-an-email", "12345")
print("Success:", success)
for message in messages:
    print("-", message)

print("\n" + "=" * 50)
print(f"Demo files are stored in: {DATA_DIR}")
print("=" * 50)