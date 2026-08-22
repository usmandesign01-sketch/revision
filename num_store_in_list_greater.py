# ask from the user to enter 5 numbers and store it in list. also tell which number is greatest

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
num4 = int(input("Enter 4th number : "))
num5 = int(input("Enter 5th number : "))

print("You enter these numbers", [num1,num2,num3,num4,num5])
if   num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print("1st number is greate: ",num1)

elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
    print("2nd number is greate: ",num2)

elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
    print("3rd number is greate: ",num3)

elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
    print("4th number is greate: ",num4)

# elif num5>num1 and num5>num2 and num5>num3 and num5>num4:
#     print("5th number is greate: ",num5)
else:
    print("5th number is greater : ",num5)

    