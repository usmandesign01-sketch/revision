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