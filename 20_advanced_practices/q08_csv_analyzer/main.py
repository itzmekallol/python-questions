"""
Q8: Simple CSV analyzer using Python's built-in csv module.
Displays row count, column count, and average/highest/lowest of a
chosen numeric column.

Run with: python main.py
"""

import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


def create_sample_csv(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "department", "salary"])
        writer.writerow(["Ananya", "Engineering", "75000"])
        writer.writerow(["Rohan", "Marketing", "48000"])
        writer.writerow(["Priya", "Engineering", "82000"])
        writer.writerow(["Vikram", "Sales", "39000"])
        writer.writerow(["Kavya", "Marketing", "55000"])


class CSVAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.rows = self._load()

    def _load(self):
        try:
            with open(self.filename, "r", newline="") as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            print(f"Error: '{self.filename}' not found")
            return []

    def row_count(self):
        return len(self.rows)

    def column_count(self):
        return len(self.rows[0]) if self.rows else 0

    def numeric_column_stats(self, column_name):
        try:
            values = [float(row[column_name]) for row in self.rows]
        except (KeyError, ValueError) as e:
            print(f"Error reading column '{column_name}': {e}")
            return None
        return {
            "average": round(sum(values) / len(values), 2),
            "highest": max(values),
            "lowest": min(values),
        }


def main():
    print("Q8: CSV analyzer")
    csv_file = path("employees.csv")
    create_sample_csv(csv_file)

    analyzer = CSVAnalyzer(csv_file)
    print("Number of rows:", analyzer.row_count())
    print("Number of columns:", analyzer.column_count())

    salary_stats = analyzer.numeric_column_stats("salary")
    print("Salary column stats:", salary_stats)


if __name__ == "__main__":
    main()
