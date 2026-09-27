# Student Academic Performance System

A modular, menu-driven Python application for managing students,
their subject-wise marks, grades, and class performance — with data
persisted to a JSON file between runs.

This project is a restructured, expanded version of a simple
single-grade student tracker: instead of one grade per student, each
student can have marks across multiple subjects, letter grades,
class-wide analysis, and generated text reports.

## Project Structure

```
Student-Academic-Performance-System/
│
├── main.py                   # Entry point: menu loop wiring everything together
│
├── student_manager.py         # Add / delete / search / display students
├── marks_manager.py           # Add / update / delete subject marks
├── grade_calculator.py        # Average + letter grade calculation
├── performance_analysis.py    # Class average, highest/lowest, subject topper
├── report_generator.py        # Build & save student/class text reports
├── validation.py              # Shared input validation helpers
├── file_handler.py            # Load/save the student database (JSON)
│
├── data/
│   └── students.json          # Persisted student database (sample data included)
│
├── tests/
│   └── test_system.py         # Unit tests for the core modules
│
└── README.md
```

## Data Model

Each student record maps subject names to marks (0-100):

```json
{
    "Alice": { "Math": 92, "Science": 88, "English": 79 },
    "Bob":   { "Math": 65, "Science": 70 }
}
```

This is a superset of the original "one grade per student" model —
a student with a single subject behaves the same way the original
script did, but the system now supports any number of subjects.

## Running the Program

From the project root:

```bash
python main.py
```

On startup the program loads `data/students.json` (creating it if
missing). On exit (menu option 15) it saves all changes back to that
file, so data persists across runs.

### Menu Options

1. Add Student
2. Delete Student
3. Search Student
4. View All Students
5. Add/Update Subject Marks
6. Delete Subject
7. View Student Marks
8. Student Grade (average + letter grade)
9. Class Average
10. Highest Performer
11. Lowest Performer
12. Subject Topper
13. Generate Student Report (optionally saved to `reports/`)
14. Generate Class Report (optionally saved to `reports/`)
15. Save & Exit

## Grading Scale

| Average | Grade |
|---------|-------|
| 90-100  | A+    |
| 80-89   | A     |
| 70-79   | B     |
| 60-69   | C     |
| 50-59   | D     |
| 40-49   | E     |
| 0-39    | F     |

## Running Tests

From the project root:

```bash
python -m unittest tests/test_system.py
```

or, to run every test in the `tests/` folder:

```bash
python -m unittest discover tests
```

## Notes

- Marks are validated to be between 0 and 100 wherever they're entered.
- `file_handler.py` gracefully handles a missing or corrupted
  `students.json` by starting from an empty database instead of
  crashing.
- Generated reports are written to a `reports/` folder (created
  automatically) and are not tracked in `data/`.
