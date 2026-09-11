
'''🏆 Day 1 Final Challenge

Make a small Student Information Program.

Ask for:

Name
Age
Class
City
Math marks
Computer marks

Then calculate:

Total marks
Average marks

Finally print a clean summary using f-strings.'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
clas = input("Class: ")
city = input("Enter your city name: ")
math_marks = int(input("Enter your maths marks: "))
computer_marks = int(input("Enter your computer marks: "))

print("\n")

print(f"Your name is {name}")
print(f"Your age is {age}")
print(f"Class {clas}")
print(f"Living in {city}")
print(f"Your math marks {math_marks}")
print(f"Your Computer marks {computer_marks}")
print(f"Total marks are {math_marks + computer_marks}")
print(f"Total avg are {(math_marks + computer_marks)/2}")

