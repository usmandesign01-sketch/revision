# Counter:
# A counter is simply a variable used to keep track of how many times somethings happens.

# Basic pattern:
# count = 0

# count +=1
# count +=1
# count +=1

# print(count) # output 3

'''
Counter inside a Loop

'''
# count = 0
# for i in range(5):
#     count += 1
# print(count)

'''
Accumulator
An accumulator is a variable that gradually build the total/result

Basic example:
total = 0

total += 10
total += 20
total += 30

print(total) # Output 60
'''
# num = [10,23,45,67,90,-23]
# total = 0
# for x in num:
#     total = total + x
# print(total)

# Accumulator answers: HOW MUCH?/ WHAT IS THE TOTAL?

# EXAMPLES:
# Total salary
# Total money
# Total price

# SUMMARY: COUNTER COUNT THINGS AND ACCUMULATOR COUNT TOTAL

print("====This is EXAMPLE of accumulator and counter====")
user_entered = []
total = 0
total_even = 0
for i in range(6):
    user = int(input(f"Enter a number {i + 1}: "))
    user_entered.append(user)
print()
print(f"You enter these number {user_entered}")

for x in user_entered:
    total = total + x

    if x % 2 == 0:
        total_even += 1

print("\n----- Result -----")
print(f"Total: {total}")
print(f"Total_odd: {total_even}")


# **************************************************************************************************************
# Create an empty list to store the numbers
numbers = []

# Take 5 numbers from the user
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Accumulator: used to calculate the total
total = 0

# Counters: used to count even and odd numbers
even_count = 0
odd_count = 0

# Go through each number in the list
for num in numbers:

    # Add the current number to the total
    total += num

    # Check whether the number is even or odd
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Calculate the average
average = total / len(numbers)

# Display the results
print("\n----- Result -----")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")