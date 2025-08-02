import json
import csv
import os

DATA_DIR = "data"
OUTPUT_DIR = "output/reports"

def load_students_json(filename=f"{DATA_DIR}/students.json"):
    """Load student data from a JSON file."""
    try:
        with open(filename, "r") as f:
            students = json.load(f)
        return students
    except FileNotFoundError:
        print(f"File {filename} not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. Returning empty list.")
        return []

def save_students_json(students, filename=f"{DATA_DIR}/students.json"):
    """Save student data to a JSON file."""
    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=4)
        print(f"Saved {len(students)} students to {filename}")
    except Exception as e:
        print(f"Error saving to {filename}: {e}")

def export_to_csv(data, headers, filename):
    """Export a list of dictionaries to a CSV file with given headers."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with open(filepath, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Exported data to {filepath}")
    except Exception as e:
        print(f"Error exporting CSV to {filepath}: {e}")

def export_gpa_leaderboard(students, filename="top_students.csv"):
    """Export top students by GPA to CSV."""
    # Sort descending by GPA
    sorted_students = sorted(students, key=lambda s: s.get('GPA', 0), reverse=True)
    headers = ['name', 'GPA']
    data = [{'name': s['name'], 'GPA': s.get('GPA', 0)} for s in sorted_students]
    export_to_csv(data, headers, filename)

def export_attendance_report(students, filename="attendance_report.csv"):
    """Export attendance summary to CSV."""
    headers = ['name', 'attendance_percent']
    data = [{'name': s['name'], 'attendance_percent': s.get('attendance_percent', 0)} for s in students]
    export_to_csv(data, headers, filename)
