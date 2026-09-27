"""
file_handler.py
----------------
Handles reading and writing the student database to a JSON file
so data survives between program runs.

Data shape stored in students.json:
{
    "Alice": {"Math": 90, "Science": 85},
    "Bob":   {"Math": 70}
}
"""

import json
import os

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "students.json")


def ensure_data_dir():
    """Make sure the data/ folder exists before reading or writing."""
    os.makedirs(DATA_DIR, exist_ok=True)


def load_data(path=DATA_FILE):
    """Load the student database from disk. Returns an empty dict if the
    file does not exist yet or is corrupted."""
    ensure_data_dir()

    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
    except (json.JSONDecodeError, OSError):
        print("Warning: students.json could not be read. Starting with an empty database.")
        return {}


def save_data(students, path=DATA_FILE):
    """Save the student database to disk."""
    ensure_data_dir()
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(students, f, indent=4)
        return True
    except OSError as e:
        print(f"Error saving data: {e}")
        return False
