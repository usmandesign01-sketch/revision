'''Student Management Program

Create a Student Management Program.

Start with:

students = []

Ask the user to enter 3 students.

For each student, store:

name
age
marks

as a dictionary.

'''

students = []

for i in range(3):
    print(f"Enter details for student {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    marks = float(input("Marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)

print("\nStudent Details:")
for student in students:
    for key, value in student.items():
        print(f"{key}: {value}")
    print()