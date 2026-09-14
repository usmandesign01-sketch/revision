user1 = int(input("Enter first number: "))
user2 = int(input("Enter 2nd number: "))
def num(user1,user2):
    if user1>user2:
        print("1st number is greater")
    elif user1==user2:
        print("Both number are same")
    else:
        print("2nd number is greater")
num(user1,user2)