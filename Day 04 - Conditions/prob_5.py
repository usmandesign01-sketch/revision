'''🔥 Day 4 — Extra Practice
🟢 Problem 1 — Number Checker

Check weather the number is positive negative or zero 
'''

num_chec = int(input("Enter a number: "))
if num_chec > 0 :
    print(f"The number you enter is positive {num_chec}")
elif num_chec < 0:
    print(f"The number you enter is negative {num_chec}")
else:
    print(f"You entered zero number {num_chec}")