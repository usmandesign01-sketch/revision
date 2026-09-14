'''Problem 6 — Three Numbers 😈
Ask the user for three numbers.
Determine which number is the largest.
Don't use:
max()
You must use conditions.
This is important because I want to see whether you can actually reason with comparisons.'''

print("=======Enter three different numbers=======")
print()
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a > b and a > c:
    print("First number is greater", a)

elif b > a and b > c:
    print("Second number is greater", b)

elif c > a and c > b:
    print("third number is greater.", c)
else:
    print("Program completed")