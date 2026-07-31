"""
Q6: Read a large text file lazily using a generator, and count total
lines, words, and characters WITHOUT loading the whole file into
memory at once.

Run with: python main.py
"""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


def lazy_line_reader(filename):
    """Yields one line at a time; the file is never fully materialized in memory."""
    with open(filename, "r") as f:
        for line in f:
            yield line


def analyze_file_lazily(filename):
    total_lines = 0
    total_words = 0
    total_characters = 0

    for line in lazy_line_reader(filename):
        total_lines += 1
        total_words += len(line.split())
        total_characters += len(line)

    return total_lines, total_words, total_characters


def create_sample_file(filename, num_lines=1000):
    with open(filename, "w") as f:
        for i in range(1, num_lines + 1):
            f.write(f"This is line number {i} of the sample large text file.\n")


def main():
    print("Q6: Lazy file reader")
    sample_file = path("large_sample.txt")
    create_sample_file(sample_file, num_lines=1000)

    lines, words, characters = analyze_file_lazily(sample_file)
    print("Total lines:", lines)
    print("Total words:", words)
    print("Total characters:", characters)


if __name__ == "__main__":
    main()
