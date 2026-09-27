"""
performance_analysis.py
------------------------
Class-wide statistics: overall average, top/bottom performers,
and subject-level toppers.
"""

from grade_calculator import get_all_averages


def class_average(students):
    """Average of all students' averages."""
    averages = get_all_averages(students)
    if not averages:
        print("No students found.")
        return 0.0

    overall = sum(averages.values()) / len(averages)
    print(f"Class Average: {overall:.2f}")
    return round(overall, 2)


def highest_performer(students):
    """Student(s) with the highest average marks."""
    averages = get_all_averages(students)
    if not averages:
        print("No students found.")
        return None

    top_score = max(averages.values())
    top_students = [name for name, avg in averages.items() if avg == top_score]

    for name in top_students:
        print(f"Highest Average: {name} - {top_score:.2f}")

    return top_students, round(top_score, 2)


def lowest_performer(students):
    """Student(s) with the lowest average marks."""
    averages = get_all_averages(students)
    if not averages:
        print("No students found.")
        return None

    low_score = min(averages.values())
    low_students = [name for name, avg in averages.items() if avg == low_score]

    for name in low_students:
        print(f"Lowest Average: {name} - {low_score:.2f}")

    return low_students, round(low_score, 2)


def subject_topper(students, subject):
    """The student with the highest marks in one particular subject."""
    scores = {
        name: marks[subject]
        for name, marks in students.items()
        if subject in marks
    }

    if not scores:
        print(f"No marks recorded for subject '{subject}'.")
        return None

    top_name = max(scores, key=scores.get)
    print(f"Topper in {subject}: {top_name} - {scores[top_name]}")
    return top_name, scores[top_name]


def top_n_performers(students, n=3):
    """Top n students ranked by average marks, highest first."""
    averages = get_all_averages(students)
    ranked = sorted(averages.items(), key=lambda item: item[1], reverse=True)
    return ranked[:n]
