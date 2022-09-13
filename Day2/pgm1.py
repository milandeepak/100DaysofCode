#  Write a program that adds the digits in a 2 digit number.
#  e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
num_str = str(two_digit_number)
num1 = int(num_str[0])
num2 = int(num_str[1])
print(num1 + num2)