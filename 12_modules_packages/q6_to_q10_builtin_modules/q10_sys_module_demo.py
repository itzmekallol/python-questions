"""
q10_sys_module_demo.py

Q10: Uses the sys module to display the Python version, command-line
arguments, and the module search path.

Run with: python q10_sys_module_demo.py arg1 arg2
"""

import sys

print("Q10: Built-in sys module")
print("Python version:", sys.version)
print("Command-line arguments:", sys.argv)
print("Module search path (first 3 entries):")
for entry in sys.path[:3]:
    print(" -", entry)
