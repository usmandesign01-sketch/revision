'''🟡 Problem 3 — Login System 🔐'''


print("=====Login System=====")
username = input("ENTER USERNAME : ")
password = int(input("ENTER PASSWORD : "))

correct_username = "usman"
correct_password = "123"

if username != correct_username and password != correct_password:
    print("Wrong username or password")
else:
    print("Login successful")