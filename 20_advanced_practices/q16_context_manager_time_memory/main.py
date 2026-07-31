"""
Q16: A context manager that measures execution time and memory usage
of the code inside a `with` block.

Uses only the standard library: `time` for timing and `tracemalloc`
for memory tracking.

Run with: python main.py
"""

import time
import tracemalloc


class PerformanceMonitor:
    def __enter__(self):
        tracemalloc.start()
        self._start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = time.perf_counter() - self._start_time

        self.elapsed_seconds = elapsed
        self.current_memory_kb = current / 1024
        self.peak_memory_kb = peak / 1024

        print(f"Execution time: {elapsed:.6f} seconds")
        print(f"Current memory usage: {self.current_memory_kb:.2f} KB")
        print(f"Peak memory usage: {self.peak_memory_kb:.2f} KB")
        return False  # do not suppress exceptions


def main():
    print("Q16: Performance monitoring context manager")

    with PerformanceMonitor():
        # allocate a reasonably large list to produce a visible memory footprint
        data = [i ** 2 for i in range(500000)]
        total = sum(data)

    print("Computed sum:", total)


if __name__ == "__main__":
    main()
