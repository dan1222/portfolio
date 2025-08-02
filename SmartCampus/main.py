# main.py

from modules import storage, admin, reports
from modules.visuals import charts, turtle_draw
from modules.student import create_student, update_gpa, get_student_summary
import sys

def main_menu():
    print("\n=== SmartCampus Main Menu ===")
    print("1. Add a new student")
    print("2. Update a student")
    print("3. View student reports")
    print("4. Export reports to CSV")
    print("5. Show visualizations (charts/certificates)")
    print("6. Save data")
    print("7. Load data")
    print("0. Exit")

# ✅ Optional test section (Daniel's part demo)
# You can delete or comment this out later if not needed
test_student = create_student("Alice", 16, 3.8, 92, ["Science", "Art"])
update_gpa(test_student, 4.0)
print(get_student_summary(test_student))

def run():
    # Load students from JSON if available
    students = storage.load_students_json()

    while True:
        main_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            new_student = admin.add_student()
            students.append(new_student)
            print(f"Added student: {new_student['name']}")

        elif choice == "2":
            student_id = input("Enter student ID to update: ")
            student = admin.find_student_by_id(students, student_id)
            if student:
                admin.update_student(student)
            else:
                print("Student not found.")

        elif choice == "3":
            if not students:
                print("No student data available.")
            else:
                reports.show_gpa_ranking(students)
                reports.show_attendance_summary(students)
                reports.show_most_active_clubs(students)

        elif choice == "4":
            if not students:
                print("No student data available to export.")
            else:
                storage.export_gpa_leaderboard(students)
                storage.export_attendance_report(students)
                print("Reports exported successfully.")

        elif choice == "5":
            if not students:
                print("No student data available to visualize.")
            else:
                charts.plot_gpa_bar_chart(students)
                charts.plot_attendance_line_chart(students)
                charts.plot_club_pie_chart(students)

                # Draw certificate for top GPA student
                top_student = max(students, key=lambda s: s.get("GPA", 0))
                turtle_draw.draw_certificate(top_student["name"], top_student["GPA"])

        elif choice == "6":
            storage.save_students_json(students)
            print("Data saved successfully.")

        elif choice == "7":
            students = storage.load_students_json()
            print("Data loaded successfully.")

        elif choice == "0":
            print("Exiting SmartCampus. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
