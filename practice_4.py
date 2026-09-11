'''🔥 Problem 6 — Type Conversion Challenge

Ask the user for two numbers as input.

Print their:

Sum
Product
Average

The average should be calculated correctly even when the result is a decimal.

Example:

Enter first number: 10
Enter second number: 20

Sum: 30
Product: 200
Average: 15.0
'''
user1 = int(input("Enter first number: "))
user2 = int(input("Enter second number: "))

print(f"The sum of two number is: {user1 + user2}")
print(f"The mulitiplication of two number is: {user1 * user2}")
print(f"The average of two number is: {(user1 + user2)/2}")