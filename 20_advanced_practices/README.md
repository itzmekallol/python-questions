# Python Practice — Advanced Python (20 Questions)

This project combines everything from earlier in the series — data
structures, OOP, file handling, JSON, modules, exceptions, iterators,
generators, decorators, context managers, regex, functional
programming, and date/time — into professional-level, interview-style
problems.

Code follows PEP 8 naming conventions, separates logic into functions
and classes, and handles exceptions explicitly rather than letting
programs crash.

## Structure

Each question lives in its own folder and can be run independently:

```
python_advanced_practice/
│
├── q01_memoized_fibonacci/          Q1  — memoized Fibonacci
├── q02_custom_zip/                  Q2  — custom zip() (generator)
├── q03_custom_enumerate/            Q3  — custom enumerate() (generator)
├── q04_custom_sorted_mergesort/     Q4  — custom sorted() via Merge Sort
├── q05_immutable_class/             Q5  — immutable class (__setattr__ blocking)
│
├── q06_lazy_file_reader/            Q6  — lazy line-by-line file stats
├── q07_json_employee_stats/         Q7  — JSON employee salary report
├── q08_csv_analyzer/                Q8  — CSV analyzer (csv module)
├── q09_config_loader/               Q9  — JSON config loader with defaults
│
├── q10_hospital_management/         Q10 — Hospital Management System (OOP)
├── q11_online_shopping/             Q11 — Online Shopping System (OOP)
├── q12_movie_ticket_booking/        Q12 — Movie Ticket Booking System (OOP)
├── q13_task_management/             Q13 — Task Management System (OOP)
│
├── q14_binary_tree_iterator/        Q14 — in-order binary tree iterator
├── q15_retry_decorator/             Q15 — configurable retry decorator
├── q16_context_manager_time_memory/ Q16 — time + memory profiling context manager
├── q17_plugin_system/               Q17 — dynamic plugin loader (importlib)
│   └── plugins/                         3 example plugin modules
│
├── q18_log_analysis_tool/           Q18 — regex + generator log analyzer
├── q19_student_database_manager/    Q19 — JSON-backed student manager
│   └── student_manager.py               separated OOP module
│
└── q20_library_management_cli/      Q20 — full Library Management System
    ├── library_system/                  a real installable-style package
    │   ├── __init__.py
    │   ├── book.py
    │   ├── member.py
    │   ├── transaction.py
    │   ├── storage.py                   JSON persistence
    │   ├── logger.py                    logging setup
    │   └── library.py                   core Library class + custom exceptions
    └── main.py                          menu-driven CLI entry point
```

## How to run

`cd` into any question folder and run `main.py`:

```bash
cd q01_memoized_fibonacci
python main.py
```

```bash
cd q20_library_management_cli
python main.py
```

Every `main.py` is self-contained: it creates any files it needs
(sample text/JSON/CSV/log files) inside a local `practice_files`
folder next to itself, so nothing clutters your working directory and
you can inspect the generated data afterward.

## Notes on specific questions

- **Q2, Q3** implement `zip()` and `enumerate()` as generators, matching
  the laziness of the real built-ins.
- **Q4** implements `sorted()`'s `key=` and `reverse=` behavior on top
  of a hand-written recursive Merge Sort — no calls to the built-in
  `sorted()` or `list.sort()`.
- **Q5**'s immutability is enforced at runtime via `__setattr__` and
  `__delattr__`, not just by convention — attempting to modify or
  delete an attribute raises `AttributeError`.
- **Q9** demonstrates three scenarios: a valid-but-incomplete config
  file, a genuinely invalid JSON file, and a missing file entirely —
  all fall back to sensible defaults without crashing.
- **Q14**'s iterator does in-order traversal iteratively with an
  explicit stack (not recursively), so it's a real lazy iterator you
  can call `next()` on.
- **Q16** uses `tracemalloc` (standard library) for real memory
  measurements, not an estimate.
- **Q17** dynamically discovers plugin modules with `pkgutil` and loads
  them with `importlib.import_module` — no plugin is hard-coded by
  name in `main.py`.
- **Q18** parses log lines with a single compiled regex and streams
  through multiple files via a generator, aggregating with
  `collections.Counter`.
- **Q20** is the most complete project: a real sub-package
  (`library_system`) with its own data models, a JSON storage layer,
  a `logging`-based logger that writes to `practice_files/library.log`,
  custom exceptions per failure mode (duplicate IDs, missing
  books/members, no copies available), and a `main.py` whose
  `run_menu()` function contains the real `input()`-driven interactive
  loop as a comment, with a full scripted demo underneath it that
  exercises every feature end-to-end.
