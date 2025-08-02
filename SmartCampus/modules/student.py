# modules/student.py

def create_student(name, age, gpa, attendance_percent, clubs):
    """
    Creates a new student dictionary.
    """
    return {
        "name": name,
        "age": age,
        "GPA": gpa,
        "attendance_percent": attendance_percent,
        "clubs": clubs  # a list of strings
    }

def update_gpa(student, new_gpa):
    """
    Updates the GPA of a student.
    """
    student["GPA"] = new_gpa

def update_attendance(student, new_attendance_percent):
    """
    Updates the attendance percentage of a student.
    """
    student["attendance_percent"] = new_attendance_percent

def add_club(student, club_name):
    """
    Adds a club to the student's club list if not already added.
    """
    if club_name not in student["clubs"]:
        student["clubs"].append(club_name)

def remove_club(student, club_name):
    """
    Removes a club from the student's club list if it exists.
    """
    if club_name in student["clubs"]:
        student["clubs"].remove(club_name)

def get_student_summary(student):
    """
    Returns a short summary string of student info.
    """
    clubs = ", ".join(student["clubs"]) if student["clubs"] else "None"
    return f"{student['name']} | GPA: {student['GPA']} | Attendance: {student['attendance_percent']}% | Clubs: {clubs}"
