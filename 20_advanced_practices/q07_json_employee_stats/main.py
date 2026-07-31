"""
Q7: Read a JSON file of employee data and generate:
  - Average salary
  - Highest salary
  - Lowest salary
  - Employees grouped by department

Run with: python main.py
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


def create_sample_employee_file(filename):
    employees = [
        {"name": "Ananya", "department": "Engineering", "salary": 75000},
        {"name": "Rohan", "department": "Marketing", "salary": 48000},
        {"name": "Priya", "department": "Engineering", "salary": 82000},
        {"name": "Vikram", "department": "Sales", "salary": 39000},
        {"name": "Kavya", "department": "Marketing", "salary": 55000},
    ]
    with open(filename, "w") as f:
        json.dump(employees, f, indent=4)


def load_employees(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return []
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid JSON")
        return []


def generate_salary_report(employees):
    if not employees:
        return None

    salaries = [emp["salary"] for emp in employees]
    average_salary = sum(salaries) / len(salaries)
    highest_paid = max(employees, key=lambda emp: emp["salary"])
    lowest_paid = min(employees, key=lambda emp: emp["salary"])

    employees_by_department = {}
    for emp in employees:
        department = emp["department"]
        employees_by_department.setdefault(department, []).append(emp["name"])

    return {
        "average_salary": round(average_salary, 2),
        "highest_paid": highest_paid,
        "lowest_paid": lowest_paid,
        "employees_by_department": employees_by_department,
    }


def main():
    print("Q7: JSON employee statistics")
    employee_file = path("employees.json")
    create_sample_employee_file(employee_file)

    employees = load_employees(employee_file)
    report = generate_salary_report(employees)

    print("Average salary:", report["average_salary"])
    print("Highest paid:", report["highest_paid"])
    print("Lowest paid:", report["lowest_paid"])
    print("Employees by department:")
    for department, names in report["employees_by_department"].items():
        print(f"  {department}: {names}")


if __name__ == "__main__":
    main()
