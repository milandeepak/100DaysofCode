# Program that calculates the sum of all the even numbers from 1 to 100.

sum = 0
for number in range(1,101):
   if number % 2 == 0:
    sum += number
print(sum)
 