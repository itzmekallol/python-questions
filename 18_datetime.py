"""
Python Practice — Date & Time (15 Questions)
Solutions with explanations.

Run this file with: python python_datetime_practice.py

Rules followed throughout:
- Only Python's built-in `datetime` module (plus `time` for the
  stopwatch/countdown) is used — no third-party libraries.
- `datetime`/`timedelta` arithmetic is used instead of manual date math.
- Solutions are written as small, reusable functions.

Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. The
stopwatch and countdown timer use short, clearly-labeled demo durations
so the script finishes quickly; both work identically with real,
longer durations.
"""

import time
from datetime import datetime, date, timedelta

# =========================================================
# PART 1: DATE & TIME BASICS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: DATE & TIME BASICS")
print("=" * 50)

# --- Q1: Current date, time, and date+time ---
now = datetime.now()
print("\nQ1:")
print("Current date:", now.date())
print("Current time:", now.time())
print("Current date and time:", now)

# --- Q2: Individual components ---
print("\nQ2:")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# --- Q3: Parse a user-entered date DD-MM-YYYY into a datetime object ---
def parse_date(date_string):
    return datetime.strptime(date_string, "%d-%m-%Y")

# date_input = input("Enter a date (DD-MM-YYYY): ")
date_input = "15-08-2026"  # sample value
parsed_date = parse_date(date_input)
print("\nQ3: Parsed datetime object:", parsed_date)

# --- Q4: Format current date/time in several formats ---
print("\nQ4:")
print("DD-MM-YYYY:", now.strftime("%d-%m-%Y"))
print("YYYY/MM/DD:", now.strftime("%Y/%m/%d"))
print("Month Day, Year:", now.strftime("%B %d, %Y"))
print("HH:MM:SS:", now.strftime("%H:%M:%S"))

# --- Q5: Today's weekday name ---
print("\nQ5: Today's weekday:", now.strftime("%A"))


# =========================================================
# PART 2: DATE CALCULATIONS (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: DATE CALCULATIONS")
print("=" * 50)

# --- Q6: Calculate age from date of birth ---
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # subtract one year if the birthday hasn't happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# dob_input = input("Enter your date of birth (DD-MM-YYYY): ")
dob_input = "15-08-2004"  # sample value
dob = parse_date(dob_input).date()
print("\nQ6: Age:", calculate_age(dob), "years")

# --- Q7: Days between two user-entered dates ---
def days_between(date_str_1, date_str_2):
    d1 = parse_date(date_str_1).date()
    d2 = parse_date(date_str_2).date()
    return abs((d2 - d1).days)

# date1_input = input("Enter first date (DD-MM-YYYY): ")
# date2_input = input("Enter second date (DD-MM-YYYY): ")
date1_input, date2_input = "01-01-2026", "29-07-2026"  # sample values
print("\nQ7: Days between the two dates:", days_between(date1_input, date2_input))

# --- Q8: Add 30 days, ~6 months, and 1 year to today ---
today = date.today()
plus_30_days = today + timedelta(days=30)
plus_6_months = today + timedelta(days=182)  # approximate, since timedelta has no "months" unit
plus_1_year = today.replace(year=today.year + 1)

print("\nQ8:")
print("Today:", today)
print("+30 days:", plus_30_days)
print("+6 months (approx, 182 days):", plus_6_months)
print("+1 year:", plus_1_year)

# --- Q9: Leap year check ---
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("\nQ9:")
print("2028 is a leap year:", is_leap_year(2028))
print("2027 is a leap year:", is_leap_year(2027))
print("2000 is a leap year:", is_leap_year(2000))
print("1900 is a leap year:", is_leap_year(1900))

# --- Q10: Days remaining until New Year's Day ---
def days_until_new_year():
    today_date = date.today()
    next_new_year = date(today_date.year + 1, 1, 1)
    return (next_new_year - today_date).days

print("\nQ10: Days remaining until New Year's Day:", days_until_new_year())


# =========================================================
# PART 3: TIME OPERATIONS (11-12)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: TIME OPERATIONS")
print("=" * 50)

# --- Q11: Simple stopwatch ---
class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()
        print("Stopwatch started")

    def stop(self):
        self.end_time = time.perf_counter()
        print("Stopwatch stopped")

    def elapsed(self):
        if self.start_time is None or self.end_time is None:
            return "Stopwatch has not been started and stopped properly"
        return self.end_time - self.start_time

print("\nQ11: Stopwatch demo")
stopwatch = Stopwatch()
stopwatch.start()
time.sleep(1.5)  # simulating some work being timed
stopwatch.stop()
print(f"Elapsed time: {stopwatch.elapsed():.4f} seconds")

# --- Q12: Countdown timer ---
def countdown_timer(seconds):
    """
    Displays the remaining time every second until it reaches zero.
    Using a short duration here (5 seconds) so the demo finishes quickly;
    this works identically with any real user-provided duration, e.g.:

    seconds = int(input("Enter countdown duration in seconds: "))
    """
    remaining = seconds
    while remaining > 0:
        print(f"Time remaining: {remaining} second(s)")
        time.sleep(1)
        remaining -= 1
    print("Countdown complete!")

print("\nQ12: Countdown timer demo (5 seconds)")
countdown_timer(5)


# =========================================================
# PART 4: REAL-WORLD MINI PROJECTS (13-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q13: Attendance Tracker ---
class AttendanceTracker:
    def __init__(self):
        self.records = {}  # name -> {"check_in": datetime, "check_out": datetime}

    def check_in(self, name, check_in_time):
        self.records[name] = {"check_in": check_in_time, "check_out": None}

    def check_out(self, name, check_out_time):
        if name in self.records:
            self.records[name]["check_out"] = check_out_time

    def working_hours(self, name, standard_hours=8):
        record = self.records.get(name)
        if not record or record["check_out"] is None:
            return None, None
        duration = record["check_out"] - record["check_in"]
        total_hours = duration.total_seconds() / 3600
        overtime = max(0, total_hours - standard_hours)
        return round(total_hours, 2), round(overtime, 2)

print("\nQ13: Attendance Tracker")
tracker = AttendanceTracker()

today_date = date.today()
tracker.check_in("Ananya", datetime.combine(today_date, datetime.min.time().replace(hour=9)))
tracker.check_out("Ananya", datetime.combine(today_date, datetime.min.time().replace(hour=18, minute=30)))

hours_worked, overtime_hours = tracker.working_hours("Ananya")
print(f"Ananya - Total hours worked: {hours_worked}, Overtime: {overtime_hours}")

# --- Q14: Event Reminder ---
class EventReminder:
    def __init__(self):
        self.events = []  # list of dicts: name, datetime

    def add_event(self, name, event_date, event_time):
        event_datetime = datetime.combine(event_date, event_time)
        self.events.append({"name": name, "datetime": event_datetime})

    def upcoming_events(self):
        now_dt = datetime.now()
        return sorted(
            [e for e in self.events if e["datetime"] >= now_dt],
            key=lambda e: e["datetime"],
        )

    def overdue_events(self):
        now_dt = datetime.now()
        return sorted(
            [e for e in self.events if e["datetime"] < now_dt],
            key=lambda e: e["datetime"],
        )

    def days_remaining(self, event):
        return (event["datetime"].date() - date.today()).days

print("\nQ14: Event Reminder")
reminder = EventReminder()
reminder.add_event("Team Meeting", today_date + timedelta(days=3), datetime.min.time().replace(hour=10))
reminder.add_event("Project Deadline", today_date + timedelta(days=10), datetime.min.time().replace(hour=17))
reminder.add_event("Past Workshop", today_date - timedelta(days=5), datetime.min.time().replace(hour=14))

print("Upcoming events:")
for event in reminder.upcoming_events():
    print(f"- {event['name']} on {event['datetime'].strftime('%d-%m-%Y %H:%M')} "
          f"({reminder.days_remaining(event)} day(s) remaining)")

print("Overdue events:")
for event in reminder.overdue_events():
    print(f"- {event['name']} was on {event['datetime'].strftime('%d-%m-%Y %H:%M')}")

# --- Q15: Digital Calendar & Appointment Scheduler ---
class AppointmentScheduler:
    def __init__(self):
        self.appointments = []  # list of dicts: title, datetime

    def add_appointment(self, title, appointment_date, appointment_time):
        appointment_datetime = datetime.combine(appointment_date, appointment_time)
        if appointment_datetime < datetime.now():
            return f"Error: Cannot schedule '{title}' in the past"
        self.appointments.append({"title": title, "datetime": appointment_datetime})
        self.appointments.sort(key=lambda a: a["datetime"])
        return f"Appointment '{title}' added"

    def view_all(self):
        return self.appointments

    def search_by_date(self, search_date):
        return [a for a in self.appointments if a["datetime"].date() == search_date]

    def delete_appointment(self, title):
        original_count = len(self.appointments)
        self.appointments = [a for a in self.appointments if a["title"] != title]
        return len(self.appointments) < original_count

    def todays_appointments(self):
        return self.search_by_date(date.today())

    def next_upcoming(self):
        now_dt = datetime.now()
        future = [a for a in self.appointments if a["datetime"] >= now_dt]
        return future[0] if future else None

print("\nQ15: Digital Calendar & Appointment Scheduler")
scheduler = AppointmentScheduler()

print(scheduler.add_appointment("Dentist Visit", today_date + timedelta(days=2),
                                 datetime.min.time().replace(hour=11)))
print(scheduler.add_appointment("Client Call", today_date, datetime.min.time().replace(hour=15)))
print(scheduler.add_appointment("Conference", today_date + timedelta(days=7),
                                 datetime.min.time().replace(hour=9)))
print(scheduler.add_appointment("Missed Meeting", today_date - timedelta(days=1),
                                 datetime.min.time().replace(hour=10)))  # rejected: in the past

print("\nAll appointments (sorted by date and time):")
for appt in scheduler.view_all():
    print(f"- {appt['title']} at {appt['datetime'].strftime('%d-%m-%Y %H:%M')}")

print("\nToday's appointments:")
for appt in scheduler.todays_appointments():
    print(f"- {appt['title']} at {appt['datetime'].strftime('%H:%M')}")

next_appt = scheduler.next_upcoming()
print("\nNext upcoming appointment:",
      f"{next_appt['title']} at {next_appt['datetime'].strftime('%d-%m-%Y %H:%M')}" if next_appt else "None")

print("\nSearch appointments on today's date:")
for appt in scheduler.search_by_date(today_date):
    print(f"- {appt['title']}")

deleted = scheduler.delete_appointment("Client Call")
print("\n'Client Call' deleted:", deleted)
print("Remaining appointments:")
for appt in scheduler.view_all():
    print(f"- {appt['title']} at {appt['datetime'].strftime('%d-%m-%Y %H:%M')}")

print("\n" + "=" * 50)
print("All datetime demonstrations completed successfully.")
print("=" * 50)