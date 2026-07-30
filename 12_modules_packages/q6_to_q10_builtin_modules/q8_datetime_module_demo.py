"""
q8_datetime_module_demo.py

Q8: Uses the datetime module to display today's date, the current
time, and calculate the number of days until a given date.
"""

from datetime import date, datetime

print("Q8: Built-in datetime module")

today = date.today()
print("Today's date:", today)

current_time = datetime.now().time()
print("Current time:", current_time.strftime("%H:%M:%S"))

target_date = date(today.year + 1, 1, 1)  # next New Year's Day
days_remaining = (target_date - today).days
print(f"Days until {target_date}: {days_remaining}")
