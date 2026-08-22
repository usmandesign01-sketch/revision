# write a program that prints a number from 1 to 20, but:
# if the number is divisible by 3 > print "Fizz"
# if divisible by 5 ? print "buzz"
# if divisible by both 3 and 5 ? print "Fizzbuzz"
# other wise print the number


for i in range(1,21):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz", i)
    elif i%3 == 0:
        print("Fizz", i)
    elif i%5 == 0:
        print("Buzz", i)
    else:
        print(i)