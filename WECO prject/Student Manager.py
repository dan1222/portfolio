class Student:
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.courses = []  # List to store enrolled courses

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}.")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} dropped {course}.")
        else:
            print(f"{self.name} is not enrolled in {course}.")

    def view_courses(self):
        if not self.courses:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            print(f"{self.name}'s Enrolled Courses:")
            for course in self.courses:
                print(f"- {course}")

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

class System:
    def __init__(self):
        self.students = []
        self.courses = []

    def run(self):
        while True:
            print("\nStudent Management System")
            print("1. Admin Menu")
            print("2. Student Menu")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.admin_menu()
            elif choice == '2':
                self.student_menu()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. List Students")
            print("4. Add Course")
            print("5. Remove Course")
            print("6. List Courses")
            print("7. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student name: ")
                student_id = input("Enter student ID: ")
                email = input("Enter student email: ")
                student = Student(name, student_id, email)
                self.students.append(student)
                print(f"Student {name} added.")
            elif choice == '2':
                student_id = input("Enter student ID to remove: ")
                for i, student in enumerate(self.students):
                    if student.student_id == student_id:
                        del self.students[i]
                        print(f"Student with ID {student_id} removed.")
                        break
                else:
                    print(f"No student found with ID {student_id}.")
            elif choice == '3':
                if not self.students:
                    print("No students in the system.")
                else:
                    print("List of Students:")
                    for student in self.students:
                        print(f"- {student.name} ({student.student_id})")
            elif choice == '4':
                course_code = input("Enter course code: ")
                course_name = input("Enter course name: ")
                course = Course(course_code, course_name)
                self.courses.append(course)
                print(f"Course {course_name} added.")
            elif choice == '5':
                course_code = input("Enter course code to remove: ")
                for i, course in enumerate(self.courses):
                    if course.course_code == course_code:
                        del self.courses[i]
                        print(f"Course {course_code} removed.")
                        break
                else:
                    print(f"No course found with code {course_code}.")
            elif choice == '6':
                if not self.courses:
                    print("No courses in the system.")
                else:
                    print("List of Courses:")
                    for course in self.courses:
                        print(f"- {course}")
            elif choice == '7':
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")

    def student_menu(self):
        while True:
            print("\nStudent Menu")
            student_id = input("Enter your student ID: ")
            student = self.find_student(student_id)
            if student:
                print("1. View Enrolled Courses")
                print("2. Enroll in Course")
                print("3. Drop Course")
                print("4. Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == '1':
                    student.view_courses()
                elif choice == '2':
                    course_code = input("Enter course code to enroll: ")
                    for course in self.courses:
                        if course.course_code == course_code:
                            student.enroll(course)
                            break
                    else:
                        print(f"No course found with code {course_code}.")
                elif choice == '3':
                    course_code = input("Enter course code to drop: ")
                    student.drop(Course(course_code, ""))  # Pass course code only
                elif choice == '4':
                    print("Returning to Main Menu.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print(f"No student found with ID {student_id}.")
                break

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

# Main program
system = System()
system.run()