'''🔥 Day 4 Final Challenge — Student Result
Now combine what you've revised so far.
Ask the student for:
Name
Math marks
Computer marks
English marks
Calculate:
Total
Average
Then determine the grade:
90+ → A+
80–89 → A
70–79 → B
60–69 → C
50–59 → D
Below 50 → F
Finally, print a clean result such as:
----- Student Result -----

Name: Usman
Math: 78
Computer: 85
English: 72

Total: 235
Average: 78.33
Grade: B
😈 Extra condition
Also determine whether the student passed or failed.
For this exercise, use:
Average >= 50 → Passed
Average < 50 → Failed'''

# ************************************************************************************************************

# name = input("Enter name: ")
# math_marks = int(input("enter maths marks: "))
# computer_marks = int(input("enter computer marks: "))
# english_marks = int(input("enter english marks: "))

# total = math_marks + computer_marks + english_marks
# print(f"Total numbers are {total}")

# average = total/3
# print(f"Total average {average}")


# # NOW FIND GRADE

# if math_marks > 100 or computer_marks > 100 or english_marks > 100: 
#     print("Invalid entry")
    
# elif 90 <= average <= 100:
#     print("Grade A+")
# elif 80 <= average <= 89:
#     print("Grade A")
# elif 70 <= average <= 79:
#     print("Grade B")
# elif 60 <= average <= 69:
#     print("Grade C")
# elif 50 <= average <= 59:
#     print("Grade D")
# else:
#     print("Grade F")

# if average >= 50:
#     print("Pass")
# else:
#     print("fail")

name = input("Enter name: ")

# Check name
if not name.isalpha():
    print("Invalid entry! Name must contain letters only.")
    exit()

math_marks = int(input("Enter maths marks: "))
computer_marks = int(input("Enter computer marks: "))
english_marks = int(input("Enter English marks: "))

# Check marks
if (math_marks < 0 or math_marks > 100 or
    computer_marks < 0 or computer_marks > 100 or
    english_marks < 0 or english_marks > 100):

    print("Invalid entry! Marks must be between 0 and 100.")
    exit()

# Calculate total and average
total = math_marks + computer_marks + english_marks
average = total / 3

print("\n----- Student Result -----")
print(f"Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")

# Pass / Fail
if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

# Find Grade
if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")