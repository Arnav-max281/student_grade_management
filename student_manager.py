"""
student_manager.py
-------------------
Core CRUD operations on the student database.

Each student is stored as:
    students[name] = {"Subject1": marks, "Subject2": marks, ...}

This module only manages students as records (add / delete / search /
display). Subject marks themselves are managed in marks_manager.py.
"""

from validation import validate_name


def add_student(students, name):
    """Add a new student with an empty subject/marks record."""
    name = name.strip()
    if not validate_name(name):
        print("Invalid student name.")
        return False

    if name in students:
        print(f"Student '{name}' already exists.")
        return False

    students[name] = {}
    print(f"Student '{name}' added.")
    return True


def delete_student(students, name):
    """Remove a student and all their marks."""
    if name in students:
        del students[name]
        print(f"Student '{name}' has been deleted.")
        return True

    print(f"Student '{name}' not found.")
    return False


def search_student(students, name):
    """Print a single student's record, if present."""
    if name in students:
        print(f"\n{name}: {students[name]}")
        return students[name]

    print(f"Student '{name}' not found.")
    return None


def display_all_students(students):
    """Print every student and their subject marks."""
    if not students:
        print("No students found.")
        return

    print("\n===== ALL STUDENTS =====")
    for name, marks in students.items():
        if marks:
            marks_str = ", ".join(f"{subj}: {score}" for subj, score in marks.items())
        else:
            marks_str = "No marks recorded"
        print(f"{name} -> {marks_str}")


def student_exists(students, name):
    return name in students
