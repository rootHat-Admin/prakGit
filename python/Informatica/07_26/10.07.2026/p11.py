print(f" {"Topic: Function - sorted"} ".center(90, "-"))

students = [
    ("Ali", 80), 
    ("Dana", 95), 
    ("Timur", 70)
]

students = sorted(
    students,
    key=lambda students: students[1]
)

print(students)