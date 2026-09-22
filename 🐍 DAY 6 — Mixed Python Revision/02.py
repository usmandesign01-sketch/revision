'''🔥 Problem 2 — Function + List'''



# marks = [443, 520, 1008, 399, 443, 801]
# print("avg:", sum(marks) / len(marks))


marks = [443, 520, 1008, 399, 443, 801]
standard_average = sum(marks) / len(marks)
print("standard average:", standard_average)

highest_marks = max(marks)
print("highest:", highest_marks)

# what is scaled average?
# scaled average is the average of the marks after scaling them to a certain range, usually to make them comparable or to fit within a specific grading system.

scaled_avg_out_of_100 = (standard_average / highest_marks) * 100
print("scaled average out of 100:", scaled_avg_out_of_100)