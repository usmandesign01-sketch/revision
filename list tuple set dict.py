# list tuple set dict

# prayer_times = ["FAJAR", "ZOHAR", "ASAR", "ESHA", "MAGHRIB"]
# for time in prayer_times: # in this 4 line "time" is a dabba and i store the prayer_times values inside it
#     print(time)

# print(prayer_times)

# prayer_times.remove("FAJAR")
# print(prayer_times)

# prayer_times.append("WETAR")
# print(prayer_times)

# prayer_times.reverse()
# print(prayer_times)

# prayer_times.insert(0,"zekar") #first write the index number where you want to insert and then the object
# print(prayer_times)

# prayer_times.pop()
# print(prayer_times)

# prayer_times.sort()
# print(prayer_times)

# one line summary: list is changebale (mutable)

# ******************************************************************************************************************************************************************

# prayer_times = ("FAJAR", "ZOHAR", "ASAR", "ESHA", "MAGHRIB")
# for time in prayer_times: 
#     print(time)

        # prayer_times.remove("FAJAR")
        # print(prayer_times)
                                        # we can't perform these operation because tuple is not changeble (imutable)
        # prayer_times.reverse()
        # print(prayer_times)

# ******************************************************************************************************************************************************************

# prayer_times = {"FAJAR", "FAJAR", "ZOHAR", "ASAR", "ESHA", "MAGHRIB"}
# print(prayer_times)

# num = {12,13,78,78,43}
# print(num)

# num.add(3)
# print(num)

# # num.difference()

# num.clear()
# print(num)

# set1 = {1,2,3,3}
# set2 = {3,4,5}
# print(set1.union(set2))

# ******************************************************************************************************************************************************************

# dictionary
# pray_time = {
#     "fajar" : "4:50",
#     "zohar" : "1:30",
#     "asar" : "1:30",
#     "esha" : "1:30",
#     "maghrib" : "1:30"
# }
# print(pray_time)
# print(pray_time.values())
# print(pray_time["fajar"],([0]))

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))

# print("You enter these numbers",[num1,num2,num3])
# for num in num1,num2,num3:
#     print(num)

# if num1>num2 and num1>num3:
#     print("First number is greater", num1)

# elif num2>num1 and num2>num3:
#     print("Second number is greater", num2)

# else:
#     print("Third number is greater", num3)

# list_num = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# for num in list_num:
#     if num % 2 == 0:
#         count = count + num
# print(count)

numbers = [3,8,11,14,20]
total = 0
for num in numbers:
    if num % 2 == 0:
        total = total + num
print(total)