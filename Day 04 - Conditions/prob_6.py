'''🟢 Problem 2 — Age + Ticket 🎟️
Ask:
Enter your age:
Rules:
- Under 5 → "Free"
- 5–12 → "Child ticket: 100"
- 13–17 → "Teen ticket: 150"
- 18+ → "Adult ticket: 200"
Try to make the conditions yourself.'''

print("====Ticket====")
age = int(input("Enter your age: "))

if age > 2 and age < 5:
    print(f"This ticket is free")
elif age > 5 and age < 12:
    print(f"Child ticket: 100")
elif age > 13 and age < 17:
    print(f"Teen ticket: 150")
elif age > 18 :
    print(f"Adult ticket: 200")