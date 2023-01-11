# Write a Python program to get the Factorial number of given number.

user_input = int(input('enter num :'))
total = 1


for i in range(1,user_input+1):
    total = total*i

print(total)