"""
grade_calculator.py
--------------------
Turns raw subject marks into an average and a letter grade.
"""

GRADE_BOUNDARIES = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (40, "E"),
    (0, "F"),
]


def calculate_average(marks_dict):
    """Average of a student's subject marks. Returns 0.0 if no marks."""
    if not marks_dict:
        return 0.0
    return sum(marks_dict.values()) / len(marks_dict)


def marks_to_letter_grade(average):
    """Convert a numeric average into a letter grade."""
    for boundary, letter in GRADE_BOUNDARIES:
        if average >= boundary:
            return letter
    return "F"


def get_student_grade(students, name):
    """Return (average, letter_grade) for one student."""
    if name not in students:
        print(f"Student '{name}' not found.")
        return None

    average = calculate_average(students[name])
    letter = marks_to_letter_grade(average)
    return round(average, 2), letter


def get_all_averages(students):
    """Return {name: average} for every student."""
    return {name: calculate_average(marks) for name, marks in students.items()}
