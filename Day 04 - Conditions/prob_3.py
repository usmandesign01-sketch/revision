'''Problem 5 — Login Check
Create:
correct_username = "usman"
correct_password = "1234"
Ask the user for username and password.
If both are correct:
Login successful
Otherwise:
Invalid username or password
This is your first exercise using and.'''



username = input("Enter the username: ")
password = int(input("Enter your password: "))

correct_username = "usman"
correct_password = "1234"

if username == "usman" and password == 1234:
    print("Access granted")
else:
    print("Incorrect username or password")


