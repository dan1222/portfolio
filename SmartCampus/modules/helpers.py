def validate_student_data(student):
    """Basic checks on student data structure."""
    required_keys = {'name', 'GPA', 'attendance_percent', 'clubs'}
    if not all(key in student for key in required_keys):
        raise ValueError("Student data missing required fields")
    # Additional validation can be added here

# modules/helpers.py

def bubble_sort_students_by_gpa(students):
    """Sort students in place by GPA descending using bubble sort."""
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j].get("GPA", 0) < students[j + 1].get("GPA", 0):
                students[j], students[j + 1] = students[j + 1], students[j]

def linear_search_by_name(students, name):
    """Return student matching name or None."""
    for student in students:
        if student.get("name", "").lower() == name.lower():
            return student
    return None
