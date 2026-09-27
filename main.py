"""
main.py
--------
Entry point for the Student Academic Performance System.
Loads data on startup, drives the menu, saves data on exit.
"""

from file_handler import load_data, save_data
from validation import get_non_empty_string, get_valid_int_input
from student_manager import (
    add_student,
    delete_student,
    search_student,
    display_all_students,
)
from marks_manager import add_marks, update_marks, delete_subject, view_marks
from grade_calculator import get_student_grade
from performance_analysis import (
    class_average,
    highest_performer,
    lowest_performer,
    subject_topper,
)
from report_generator import (
    generate_student_report,
    generate_class_report,
    save_report_to_file,
)


def print_menu():
    print("\n===== STUDENT ACADEMIC PERFORMANCE SYSTEM =====")
    print(" 1. Add Student")
    print(" 2. Delete Student")
    print(" 3. Search Student")
    print(" 4. View All Students")
    print(" 5. Add/Update Subject Marks")
    print(" 6. Delete Subject")
    print(" 7. View Student Marks")
    print(" 8. Student Grade")
    print(" 9. Class Average")
    print("10. Highest Performer")
    print("11. Lowest Performer")
    print("12. Subject Topper")
    print("13. Generate Student Report")
    print("14. Generate Class Report")
    print("15. Save & Exit")


def main():
    students = load_data()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = get_non_empty_string("Enter student name: ")
            add_student(students, name)

        elif choice == "2":
            name = get_non_empty_string("Enter student name to delete: ")
            delete_student(students, name)

        elif choice == "3":
            name = get_non_empty_string("Enter student name to search: ")
            search_student(students, name)

        elif choice == "4":
            display_all_students(students)

        elif choice == "5":
            name = get_non_empty_string("Enter student name: ")
            subject = get_non_empty_string("Enter subject name: ")
            marks = get_valid_int_input("Enter marks (0-100): ", 0, 100)
            if subject in students.get(name, {}):
                update_marks(students, name, subject, marks)
            else:
                add_marks(students, name, subject, marks)

        elif choice == "6":
            name = get_non_empty_string("Enter student name: ")
            subject = get_non_empty_string("Enter subject to delete: ")
            delete_subject(students, name, subject)

        elif choice == "7":
            name = get_non_empty_string("Enter student name: ")
            view_marks(students, name)

        elif choice == "8":
            name = get_non_empty_string("Enter student name: ")
            result = get_student_grade(students, name)
            if result:
                average, letter = result
                print(f"{name} -> Average: {average}, Grade: {letter}")

        elif choice == "9":
            class_average(students)

        elif choice == "10":
            highest_performer(students)

        elif choice == "11":
            lowest_performer(students)

        elif choice == "12":
            subject = get_non_empty_string("Enter subject name: ")
            subject_topper(students, subject)

        elif choice == "13":
            name = get_non_empty_string("Enter student name: ")
            report = generate_student_report(students, name)
            if report and input("Save this report to a file? (y/n): ").lower() == "y":
                save_report_to_file(report, filename=f"{name}_report.txt")

        elif choice == "14":
            report = generate_class_report(students)
            if report and input("Save this report to a file? (y/n): ").lower() == "y":
                save_report_to_file(report, filename="class_report.txt")

        elif choice == "15":
            save_data(students)
            print("Data saved. Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
