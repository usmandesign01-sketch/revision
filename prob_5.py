'''Ask the user for:

Name
Age
Favorite number

Then print something like:

Usman is 18 years old.
His favorite number is 7.
If we add his age and favorite number, the result is 25.'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
fvt_number = int(input("Enter fvt number: "))

print("Name:",name,"\n", "Age:",age,"\n", "If we add your fvt number to your age then your age will become",fvt_number+age)