"""
Q18: Log Analysis Tool.

Reads one or more log files and generates a report showing total
requests, error count, most common IP address, most common URL, and
status code distribution.

Uses regular expressions, generators, and dictionaries as required.

Run with: python main.py
"""

import os
import re
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


LOG_LINE_PATTERN = re.compile(
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s.*\[(?P<date>[^\]]+)\]\s'
    r'"[A-Z]+\s(?P<url>\S+)\sHTTP/[\d.]+"\s(?P<status>\d{3})'
)


def create_sample_log_files():
    log1 = """\
192.168.1.10 - - [29/Jul/2026:09:00:01] "GET /index.html HTTP/1.1" 200
192.168.1.15 - - [29/Jul/2026:09:01:22] "GET /about.html HTTP/1.1" 200
10.0.0.5 - - [29/Jul/2026:09:02:47] "POST /login HTTP/1.1" 401
192.168.1.10 - - [29/Jul/2026:09:03:10] "GET /dashboard HTTP/1.1" 200
"""
    log2 = """\
172.16.0.3 - - [29/Jul/2026:09:04:35] "GET /missing-page HTTP/1.1" 404
10.0.0.5 - - [29/Jul/2026:09:05:59] "POST /login HTTP/1.1" 200
192.168.1.10 - - [29/Jul/2026:09:06:12] "GET /index.html HTTP/1.1" 200
192.168.1.15 - - [29/Jul/2026:09:07:40] "GET /api/data HTTP/1.1" 500
192.168.1.10 - - [29/Jul/2026:09:08:02] "GET /index.html HTTP/1.1" 200
"""
    with open(path("access1.log"), "w") as f:
        f.write(log1)
    with open(path("access2.log"), "w") as f:
        f.write(log2)
    return [path("access1.log"), path("access2.log")]


def parsed_log_lines(filenames):
    """
    A generator that lazily reads through every log file, line by
    line, and yields parsed match dictionaries. Nothing is loaded into
    memory beyond one line at a time per file.
    """
    for filename in filenames:
        with open(filename, "r") as f:
            for line in f:
                match = LOG_LINE_PATTERN.match(line)
                if match:
                    yield match.groupdict()


def analyze_logs(filenames):
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()
    total_requests = 0

    for entry in parsed_log_lines(filenames):
        total_requests += 1
        ip_counter[entry["ip"]] += 1
        url_counter[entry["url"]] += 1
        status_counter[entry["status"]] += 1

    error_count = sum(count for status, count in status_counter.items() if status.startswith(("4", "5")))
    most_common_ip = ip_counter.most_common(1)[0] if ip_counter else None
    most_common_url = url_counter.most_common(1)[0] if url_counter else None

    return {
        "total_requests": total_requests,
        "error_count": error_count,
        "most_common_ip": most_common_ip,
        "most_common_url": most_common_url,
        "status_distribution": dict(status_counter),
    }


def main():
    print("Q18: Log Analysis Tool")
    log_files = create_sample_log_files()

    report = analyze_logs(log_files)

    print("\n--- Log Analysis Report ---")
    print("Total requests:", report["total_requests"])
    print("Error count (4xx/5xx):", report["error_count"])
    print("Most common IP address:", report["most_common_ip"])
    print("Most common URL:", report["most_common_url"])
    print("Status code distribution:")
    for status_code, count in sorted(report["status_distribution"].items()):
        print(f"  {status_code}: {count}")


if __name__ == "__main__":
    main()
