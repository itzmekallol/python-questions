"""
Q15: A decorator that automatically retries a function if it raises an
exception, with a configurable maximum number of retries.

Run with: python main.py
"""

import functools


def retry(max_retries=3, delay_seconds=0):
    """Decorator factory: retries the decorated function up to
    max_retries times if it raises an exception, then re-raises the
    last exception if every attempt fails."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_retries and delay_seconds:
                        import time
                        time.sleep(delay_seconds)
            print(f"All {max_retries} attempts failed.")
            raise last_exception
        return wrapper
    return decorator


# Simulate a flaky function that fails on its first two calls, then succeeds
call_counter = {"count": 0}

@retry(max_retries=4)
def unreliable_network_call():
    call_counter["count"] += 1
    if call_counter["count"] < 3:
        raise ConnectionError(f"Simulated network failure (attempt {call_counter['count']})")
    return "Data received successfully"


@retry(max_retries=2)
def always_fails():
    raise ValueError("This function always fails")


def main():
    print("Q15: Retry decorator")

    print("\n-- Function that succeeds on the 3rd attempt --")
    result = unreliable_network_call()
    print("Result:", result)

    print("\n-- Function that never succeeds (exhausts all retries) --")
    try:
        always_fails()
    except ValueError as e:
        print("Final exception raised after exhausting retries:", e)


if __name__ == "__main__":
    main()
