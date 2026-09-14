'''

Problem 4 — Marks & Grade
Ask the user for their marks.
Use these rules:

90 _ 100 → A+
80 _ 89  → A
70 _ 79  → B
60 _ 69  → C
50 _ 59  → D
Below 50 → F 

'''


marks = int(input("Enter marks out of 100: "))

if marks > 100:
    print("Invalid entry")
elif 90 <= marks <= 100:
    print("Grade A+")
elif 80 <= marks <= 89:
    print("Grade A")
elif 70 <= marks <= 79:
    print("Grade B")
elif 60 <= marks <= 69:
    print("Grade C")
elif 50 <= marks <= 59:
    print("Grade D")
else:
    print("Grade F")