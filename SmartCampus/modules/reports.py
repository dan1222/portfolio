# modules/reports.py

def show_gpa_ranking(students):
    print("\n=== GPA Ranking ===")
    # Sort students by GPA descending
    ranked = sorted(students, key=lambda s: s.get("GPA", 0), reverse=True)
    for i, student in enumerate(ranked, 1):
        print(f"{i}. {student['name']} - GPA: {student.get('GPA', 0):.2f}")

def show_attendance_summary(students):
    print("\n=== Attendance Summary ===")
    # Sort ascending by attendance_percent (lowest attendance first)
    sorted_attendance = sorted(students, key=lambda s: s.get("attendance_percent", 100))
    for student in sorted_attendance:
        print(f"{student['name']}: {student.get('attendance_percent', 0):.2f}% attendance")

def show_most_active_clubs(students):
    print("\n=== Most Active Clubs ===")
    club_counts = {}
    for s in students:
        for club in s.get("clubs", []):
            club_counts[club] = club_counts.get(club, 0) + 1
    sorted_clubs = sorted(club_counts.items(), key=lambda x: x[1], reverse=True)
    for club, count in sorted_clubs:
        print(f"{club}: {count} members")
