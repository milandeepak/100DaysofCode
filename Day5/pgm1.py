# Program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
sum = 0
for height in student_heights:
    sum = sum+n
average = sum/len(student_heights)
print(round(average))
