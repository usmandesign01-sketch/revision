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
print(num)

postive_number = []
negative_number = []
zero_are = []
even_are = []
odd_are = []

if number > 0:
    postive_number = postive_number + 1 
    print(number)
else:
    negative_number = negative_number + 1
    print(number)
if number == 0:
    zero_are = zero_are + 1
    print(number)
if number % 2 == 0:
    even_are = even_are + 1
    print(number)
else:
    odd_are = odd_are + 1
    print(number)



