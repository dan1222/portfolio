# modules/admin.py

def add_student():
    """Create a new student dictionary with input prompts."""
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    # Start with empty scores, clubs, and attendance
    student = {
        "id": student_id,
        "name": name,
        "scores": [],
        "clubs": set(),
        "attendance": [],
        "GPA": 0.0,
        "attendance_percent": 0.0,
    }
    print(f"Student {name} added.")
    return student

def find_student_by_id(students, student_id):
    """Return the student dict matching the student_id or None."""
    for student in students:
        if student.get("id") == student_id:
            return student
    return None

def update_student(student):
    """Menu to update a student’s scores, attendance, and clubs."""

    while True:
        print(f"\nUpdating {student['name']}")
        print("1. Add a test score")
        print("2. Update attendance (present=1, absent=0)")
        print("3. Add club")
        print("4. Remove club")
        print("5. Calculate GPA and attendance percent")
        print("0. Return to main menu")
        choice = input("Choice: ").strip()

        if choice == "1":
            try:
                score = float(input("Enter test score (0-100): "))
                if 0 <= score <= 100:
                    student["scores"].append(score)
                    print(f"Score {score} added.")
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score input.")

        elif choice == "2":
            att = input("Enter attendance (P for present, A for absent): ").strip().upper()
            if att == "P":
                student["attendance"].append(True)
                print("Marked present.")
            elif att == "A":
                student["attendance"].append(False)
                print("Marked absent.")
            else:
                print("Invalid input. Use P or A.")

        elif choice == "3":
            club = input("Enter club name to add: ").strip()
            student["clubs"].add(club)
            print(f"Added club: {club}")

        elif choice == "4":
            club = input("Enter club name to remove: ").strip()
            if club in student["clubs"]:
                student["clubs"].remove(club)
                print(f"Removed club: {club}")
            else:
                print(f"{club} not found in student clubs.")

        elif choice == "5":
            # Calculate GPA (average of scores)
            if student["scores"]:
                student["GPA"] = sum(student["scores"]) / len(student["scores"])
            else:
                student["GPA"] = 0.0

            # Calculate attendance percentage
            if student["attendance"]:
                attended = sum(student["attendance"])
                total = len(student["attendance"])
                student["attendance_percent"] = (attended / total) * 100
            else:
                student["attendance_percent"] = 0.0

            print(f"Updated GPA: {student['GPA']:.2f}")
            print(f"Attendance: {student['attendance_percent']:.2f}%")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")
