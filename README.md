# Student Manager App

A simple command-line application built in Python to manage student records — add, view, update, delete students, and check their results. Data is saved persistently using JSON, so records are available even after restarting the program.

## Features

- **Add Student** — Add a new student with their name and marks
- **View Students** — View all students along with their marks, plus automatically calculated **average**, **highest**, and **lowest** marks
- **Check Results** — Look up a specific student and see their grade (A / B / C / FAIL) based on marks
- **Update Marks** — Update the marks of an existing student without re-adding them
- **Delete Student** — Remove a student's record
- **Persistent Storage** — All data is saved to `students.json`, so records are not lost when the program exits

## Grading Scale

| Marks Range | Grade |
|-------------|-------|
| 80 and above | A (PASS) |
| 60 - 79 | B (PASS) |
| 40 - 59 | C (PASS) |
| Below 40 | FAIL |

## How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Run the script:

```bash
python3 project_1.py
```

4. Follow the on-screen menu to add, view, update, delete, or check student records.

## Example

```
-----STUDENT MANAGER APP-----
1. Add Student
2. View Students
3. Check Results
4. Update Marks
5. Delete Student
6. Exit
Enter your choice: 1
Enter Student Name: Antor
Enter marks: 85
Antor Successfully added!
```

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON file (`students.json`)
- **Concepts used:** Dictionaries, file I/O, exception handling (`try/except`), control flow (loops, conditionals)

## Possible Future Improvements

- Support for multiple subjects per student
- Export student data to CSV
- Rewrite using Object-Oriented Programming (OOP) with a `Student` class
- Add a GUI using `tkinter` or a web interface using Flask

## Author

Md. Saifur Rahman Antor
University of Dhaka,Bangladesh
