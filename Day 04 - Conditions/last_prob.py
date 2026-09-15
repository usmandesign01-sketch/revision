'''🔴 Problem 6 — Student Result v2
This one is your Day 4 boss fight 😈
Ask for:
- Name
- Age
- Math marks
- Computer marks
- English marks
Then:
1. Check that age is reasonable.
2. Check every subject is between 0 and 100.
3. Calculate total.
4. Calculate average.
5. Print Pass/Fail.
6. Give grade:
   - 90+ → A+
   - 80+ → A
   - 70+ → B
   - 60+ → C
   - 50+ → D
   - Below 50 → F
Example
Enter name: Usman
Enter age: 19
Math: 85
Computer: 92
English: 78

----- Result -----
Name: Usman
Age: 19
Total: 255
Average: 85
Result: Pass
Grade: A'''


# import sys # import sys  # Import the system module to allow stopping the program

# print("-----Result-----")
# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))
# math_marks = int(input("Enter Your math_marks : "))
# computer_marks = int(input("Enter Your computer_marks : "))
# english_marks = int(input("Enter Your english_marks : "))

# total = math_marks + english_marks + computer_marks

# if math_marks or english_marks or computer_marks > 100:
#    print("Invalid numbers are ENTERED")
#    print("Enter Marks between 0 to 100")

#    sys.exit()
# else:
#    print("Enter detail again")

# print(f"Total Marks: {total}")
# print(f"Average Marks: {(total)/3}")


# average = total/3

# if average > 33:
#    print("Result: Pass")
# else:
#    print("Result: Fail")

#    # Now find grade

# if average > 90 and average < 100:
#    print("Grade: A+")
# elif average > 80 and average < 90:
#    print("Grade: A")
# elif average > 70 and average < 80:
#    print("Grade: B")
# elif average > 60 and average < 70:
#    print("Grade: C")
# elif average > 50 and average < 60:
#    print("Grade: C")
# elif average > 40 and average < 50:
#    print("Grade: D")
# else:
#    print("Fail")

print("-----Result-----")
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
math_marks = int(input("Enter Your math_marks : "))
computer_marks = int(input("Enter Your computer_marks : "))
english_marks = int(input("Enter Your english_marks : "))

marks = [math_marks, computer_marks, english_marks]

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks. Enter marks between 0 and 100.")
    sys.exit()

total = math_marks + computer_marks + english_marks
average = total / 3

print(f"Total Marks: {total}")
print(f"Average Marks: {average}")

if average >= 33:
    print("Result: Pass")
else:
    print("Result: Fail")

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