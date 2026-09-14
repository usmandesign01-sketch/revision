'''Problem 1 — Age Check
Ask the user for their age.
Print:
You are an adult.
if they're 18 or older.
Otherwise:
You are a minor.'''

age = int(input("Enter your age: "))
if age >= 18:
    print('You are adult')

else:
    print("You are minor")