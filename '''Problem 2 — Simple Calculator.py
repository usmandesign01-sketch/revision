'''Problem 2 — Simple Calculator

Ask the user for two numbers.

Print:

Sum:
Difference:
Multiplication:
Division:

Make sure the numbers are converted from input() into numbers.'''

user1 = int(input("Enter first number: "))
user2 = int(input("Enter second number: "))
print(f"The sum of two number is: {user1 + user2}")
print(f"The difference of two number is: {user1 - user2}")
print(f"The mulitiplication of two number is: {user1 * user2}")
if user1 == 0 or user2 == 0:
    print("Division by zero is zero")
else:
    print(f"The divison of two number is: {user1 / user2}")




