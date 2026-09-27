"""
validation.py
-------------
Reusable input validation helpers used across the system.
Keeping validation in one place avoids duplicated input-checking
logic in student_manager, marks_manager, etc.
"""


def get_non_empty_string(prompt):
    """Keep asking until the user enters a non-blank string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_valid_int_input(prompt, min_val=0, max_val=100):
    """Keep asking until the user enters an integer within [min_val, max_val]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < min_val or value > max_val:
            print(f"Value must be between {min_val} and {max_val}.")
            continue

        return value


def validate_marks(marks):
    """Return True if marks are a valid 0-100 numeric value."""
    try:
        value = float(marks)
    except (TypeError, ValueError):
        return False
    return 0 <= value <= 100


def validate_name(name):
    """A student name must be a non-empty string after stripping whitespace."""
    return isinstance(name, str) and len(name.strip()) > 0
