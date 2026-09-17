'''Problem 1 — Dictionary + Loop'''

student = {
    "name": "Usman",
    "age": 19,
    "city": "Mingora",
    "math": 50,
    "computer": 87,
    "english": 78
}

total = 0
for key, value in student.items():
    print(f"{key}: {value}")

    if key in ["math", "computer", "english"]:
        total += value
print()
print(f"Total of three subjects: {total}")
print()