'''🟢 1. Number Counter

Ask the user for 10 numbers.
Find:
- How many are positive
- How many are negative
- How many are zero
- How many are even
- How many are odd'''

# number = []
# for i in range(4):
#     num = int(input(f"Enter number {i+1}: "))
#     number.append(num)
# # print(num)

# postive_number = 0
# negative_number = 0
# zero_are = 0
# even_are = 0
# odd_are = 0

# for num in number:
#     if num > 0:
#         # print(f"Positive number: {num}")
#         postive_number += 1

#     elif num < 0:
#         # print(f"Negative number: {num}")
#         negative_number += 1

#     else:
#         print(f"Zero: {num}")
#         zero_are = zero_are + 1

#     if num % 2 == 0:
#         even_are = even_are + 1
#         # print(f"Even number: {num}")

#     else:
#         odd_are = odd_are + 1
#         # print(f"Odd number: {num}")
#     print(num)

number = []

for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)

positive_number = 0
negative_number = 0
zero_are = 0
even_are = 0
odd_are = 0

for num in number:

    # Positive, Negative, Zero
    if num > 0:
        print(f"Positive number: {num}")
        positive_number += 1

    elif num < 0:
        print(f"Negative number: {num}")
        negative_number += 1

    else:
        print(f"Zero: {num}")
        zero_are += 1

    # Even and Odd
    if num == 0:
        zero_are = zero_are  # zero already counted above

    elif num % 2 == 0:
        even_are += 1

    else:
        odd_are += 1

print("\n----- Result -----")
print(f"Positive numbers: {positive_number}")
print(f"Negative numbers: {negative_number}")
print(f"Zero: {zero_are}")
print(f"Even numbers: {even_are}")
print(f"Odd numbers: {odd_are}")

