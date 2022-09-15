# Program that picks out a random name out of a given list
import random
name_s = input("Enter some names seperated by commas:")
names = name_s.split(",")
length = len(names)
randnum = random.randint(0,length-1)
randname = names[randnum]
print(f"{randname} is going to buy the meal today!")
