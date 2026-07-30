# Python Practice — Modules & Packages (15 Questions)

This project is deliberately split into many small `.py` files and folders
instead of one big script, per the rules: each module does one job, only
the needed names are imported, and naming follows PEP 8 (lowercase,
underscore-separated module/package names).

## How to run each question

Every question folder is self-contained. `cd` into it and run `main.py`
(or the single demo file for Q6–Q10):

```
python_modules_packages_practice/
│
├── q1_calculator_module/          Q1 — calculator.py module + main.py
├── q2_geometry_module/            Q2 — geometry.py module + main.py
├── q3_number_utils_module/        Q3 — number_utils.py + selective import in main.py
├── q4_string_utils_module/        Q4 — string_utils.py + alias import in main.py
├── q5_temperature_module/         Q5 — temperature.py + all three import styles
│
├── q6_to_q10_builtin_modules/     Q6–Q10 — one file per built-in module demo
│   ├── q6_math_module_demo.py
│   ├── q7_random_module_demo.py
│   ├── q8_datetime_module_demo.py
│   ├── q9_os_module_demo.py
│   └── q10_sys_module_demo.py
│
├── q11_utilities_package/         Q11 — "utilities" package (math/string/file utils)
│   ├── utilities/
│   │   ├── __init__.py
│   │   ├── math_utils.py
│   │   ├── string_utils.py
│   │   └── file_utils.py
│   └── main.py
│
├── q12_bank_package/              Q12 — "bank" package (account/transaction/customer)
│   ├── bank/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── transaction.py
│   │   └── customer.py
│   └── main.py
│
├── q13_school_package/            Q13 — "school" package (student/teacher/classroom)
│   ├── school/
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── teacher.py
│   │   └── classroom.py
│   └── main.py
│
├── q14_my_tools_package/          Q14 — "my_tools" personal utility package + menu demo
│   ├── my_tools/
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   ├── converter.py
│   │   ├── password_generator.py
│   │   └── validator.py
│   └── main.py
│
└── q15_library_package/           Q15 — "library" management package
    ├── library/
    │   ├── __init__.py
    │   ├── book.py
    │   ├── member.py
    │   ├── library.py
    │   └── file_handler.py
    └── main.py
```

### Example

```bash
cd q1_calculator_module
python main.py
```

```bash
cd q15_library_package
python main.py
```

## Notes

- **Q3** imports only `is_prime`, `reverse_number`, and `count_digits` from
  `number_utils` — not the whole module — to demonstrate selective imports.
- **Q4** imports `string_utils` under the alias `su`.
- **Q5** shows all three import styles (`import module`,
  `from module import function`, `from module import *`) in one `main.py`
  so you can compare them directly.
- **Q9**'s `os` demo creates a folder, renames it, then deletes it, so it
  leaves your directory exactly as it found it.
- **Q14**'s menu-driven program has the real `input()`-based interactive
  loop written out inside a docstring in `run_menu()`, with a working
  non-interactive simulation underneath it so the script still runs
  end-to-end on its own.
- **Q15** follows the exact folder layout requested in the prompt,
  including a `file_handler.py` that saves/loads book records to
  `library_data.txt` (created fresh each time you run `main.py`).
