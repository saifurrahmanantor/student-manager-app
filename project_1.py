import json
import os

FILENAME = "students.json"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        student = json.load(f)
else:
    student = {}

def save_data():
    with open(FILENAME, "w") as f:
        json.dump(student, f, indent=4)

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Results")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")

        try:
            marks = int(input("Enter marks: "))
        except ValueError:
            print("Invalid marks — please enter a number.")
            continue

        if name in student:
            print(f"{name} already exists — updating marks.")

        student[name] = marks
        save_data()
        print(f"{name} Successfully added!")

    elif choice == "2":
        if not student:
            print("No Student found")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

            marks_list = list(student.values())
            average = sum(marks_list) / len(marks_list)

            highest_name = max(student, key=student.get)
            lowest_name = min(student, key=student.get)

            print(f"\nAverage Marks: {average:.2f}")
            print(f"Highest: {highest_name} ({student[highest_name]})")
            print(f"Lowest: {lowest_name} ({student[lowest_name]})")

    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 80:
                print("Grade: A (PASS)")
            elif marks >= 60:
                print("Grade: B (PASS)")
            elif marks >= 40:
                print("Grade: C (PASS)")
            else:
                print("Grade: FAIL")
        else:
            print("Student not Found")

    elif choice == "4":
        name = input("Enter student name to update: ")

        if name in student:
            try:
                new_marks = int(input("Enter new marks: "))
                student[name] = new_marks
                save_data()
                print(f"{name}'s marks updated to {new_marks}.")
            except ValueError:
                print("Invalid marks — please enter a number.")
        else:
            print("Student not Found")

    elif choice == "5":
        name = input("Enter student name to delete: ")

        if name in student:
            del student[name]
            save_data()
            print(f"{name} deleted successfully.")
        else:
            print("Student not Found")

    elif choice == "6":
        print("Exiting....")
        break

    else:
        print("Invalid Input")