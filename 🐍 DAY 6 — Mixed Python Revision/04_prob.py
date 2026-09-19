'''🟢 1. Number Counter

Ask the user for 10 numbers.
Find:
- How many are positive
- How many are negative
- How many are zero
- How many are even
- How many are odd'''

number = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)
# print(num)

postive_number = 0
negative_number = 0
zero_are = 0
even_are = 0
odd_are = 0

for num in number:
    if num > 0:
        print(f"Positive number: {num}")
        postive_number += 1

    else:
        print(f"Negative number: {num}")
        negative_number += 1

for num in number:
    if num == 0:
        zero_are = zero_are + 1
        # print(f"Zero: {num}")

    elif num % 2 == 0:
        even_are = even_are + 1
        # print(f"Even number: {num}")

    else:
        odd_are = odd_are + 1
        # print(f"Odd number: {num}")
print(num)



