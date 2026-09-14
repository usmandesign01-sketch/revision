'''🟡 Problem 5 — Simple Calculator 🧮
Ask for:
First number:
Second number:
Operation (+, -, *, /):
Then perform the selected operation.
Example:
First number: 20
Second number: 5
Operation: *

Answer: 100
You'll need conditions such as:
if operation == "+"
Also think about what should happen if the user tries to divide by zero.'''

print("Simple Calculation")

a = int(input("Enter 1st Number : "))

b = int(input("Enter 2nd Number : "))

c = input("Enter Operation (+, -, *, /): ")

if c == "+" :
    print (a+b)

elif c == "-" :
    print (a-b)

elif c == "*" :
    print (a*b)

elif c == "/" :
    if b == 0:
        print("cannot divide by zero")
    else:
        print (a/b)

else :
    print("Invalid Entry")