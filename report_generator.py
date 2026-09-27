"""
report_generator.py
---------------------
Builds human-readable reports for a single student or the whole
class, and can save them to a text file.
"""

import os
from datetime import datetime

from grade_calculator import get_student_grade
from performance_analysis import class_average, highest_performer, lowest_performer

REPORTS_DIR = "reports"


def generate_student_report(students, name):
    """Build a text report for one student. Returns the report string."""
    if name not in students:
        print(f"Student '{name}' not found.")
        return None

    result = get_student_grade(students, name)
    average, letter = result

    lines = [
        "===== STUDENT REPORT =====",
        f"Name: {name}",
        f"Subjects: {len(students[name])}",
    ]
    for subject, marks in students[name].items():
        lines.append(f"  - {subject}: {marks}")
    lines.append(f"Average: {average:.2f}")
    lines.append(f"Grade: {letter}")

    report = "\n".join(lines)
    print("\n" + report)
    return report


def generate_class_report(students):
    """Build a text report summarizing the whole class."""
    lines = ["===== CLASS REPORT =====", f"Total Students: {len(students)}"]

    if students:
        lines.append(f"Class Average: {class_average(students):.2f}")

        top = highest_performer(students)
        low = lowest_performer(students)

        if top:
            names, score = top
            lines.append(f"Top Performer(s): {', '.join(names)} ({score:.2f})")
        if low:
            names, score = low
            lines.append(f"Lowest Performer(s): {', '.join(names)} ({score:.2f})")
    else:
        lines.append("No students found.")

    report = "\n".join(lines)
    print("\n" + report)
    return report


def save_report_to_file(report_text, filename=None):
    """Save a generated report string to reports/<filename>.txt."""
    if not report_text:
        return False

    os.makedirs(REPORTS_DIR, exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.txt"

    path = os.path.join(REPORTS_DIR, filename)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(report_text)
        print(f"Report saved to {path}")
        return True
    except OSError as e:
        print(f"Error saving report: {e}")
        return False
