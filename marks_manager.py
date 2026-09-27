"""
marks_manager.py
-----------------
Manages subject-wise marks for each student
(add a subject, update marks, delete a subject).
"""

from validation import validate_marks


def add_marks(students, name, subject, marks):
    """Add or overwrite marks for a subject for the given student."""
    if name not in students:
        print(f"Student '{name}' not found.")
        return False

    if not validate_marks(marks):
        print("Marks must be a number between 0 and 100.")
        return False

    subject = subject.strip()
    students[name][subject] = marks
    print(f"{subject} marks for {name} set to {marks}.")
    return True


def update_marks(students, name, subject, marks):
    """Update marks for a subject that already exists for the student."""
    if name not in students:
        print(f"Student '{name}' not found.")
        return False

    if subject not in students[name]:
        print(f"Subject '{subject}' not found for {name}.")
        return False

    if not validate_marks(marks):
        print("Marks must be a number between 0 and 100.")
        return False

    students[name][subject] = marks
    print(f"{subject} marks for {name} updated to {marks}.")
    return True


def delete_subject(students, name, subject):
    """Remove a subject's marks from a student's record."""
    if name not in students:
        print(f"Student '{name}' not found.")
        return False

    if subject in students[name]:
        del students[name][subject]
        print(f"Subject '{subject}' removed for {name}.")
        return True

    print(f"Subject '{subject}' not found for {name}.")
    return False


def view_marks(students, name):
    """Return (and print) all subject marks for a student."""
    if name not in students:
        print(f"Student '{name}' not found.")
        return None

    marks = students[name]
    if not marks:
        print(f"{name} has no marks recorded yet.")
    else:
        print(f"\nMarks for {name}:")
        for subject, score in marks.items():
            print(f"  {subject}: {score}")

    return marks
