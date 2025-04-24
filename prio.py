class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll_no},{self.name},{self.marks}"

students = []

def add_student():
    print("Function add_student() called")
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    student = Student(roll_no, name, marks)
    students.append(student)
    print(" Student added successfully!")

def view_students():
    print("Function view_students() called")
    if not students:
        print("No student records found.")
        return
    
    print("\n Student List:")
    for student in students:
        print(student)

def search_student():
    print("Function search_student() called")
    roll_no = input("Enter Roll Number to search: ")
    found = False

    for student in students:
        if student.roll_no == roll_no:
            print(" Student Found:", student)
            found = True
            break
    
    if not found:
        print(" Student not found.")

def delete_student():
    print("Function delete_student() called")
    roll_no = input("Enter Roll Number to delete: ")
    global students
    students = [s for s in students if s.roll_no != roll_no]
    print(" Student deleted if roll number existed.")

def save_students_to_file():
    print("Function save_students_to_file() called")
    with open("students.txt", "w") as file:
        for student in students:
            file.write(str(student) + "\n")
    print(" Student data saved to 'students.txt'.")

def load_students_from_file():
    print("Function load_students_from_file() called")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll_no, name, marks = line.strip().split(",")
                students.append(Student(roll_no, name, marks))
        print(" Student data loaded successfully.")
    except FileNotFoundError:
        print(" No previous data found. Starting fresh.")

def main():
    print("Program started")
    load_students_from_file()

    while True:
        print("\n STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_students_to_file()
            print(" Exiting program. Bye!")
            break
        else:
            print(" Invalid choice. Try again.")

# Run the program
main()
