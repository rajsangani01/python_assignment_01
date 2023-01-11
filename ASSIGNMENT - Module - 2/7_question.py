# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

user_ask=int(input("enter any value:-"))

answer=user_ask%2

if answer==0:
    print("your entered value is  even:-")
else:
    print("your entered value is odd:-")