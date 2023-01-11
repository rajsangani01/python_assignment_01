# Write a Python program to unzip a list of tuples into individual lists.

x = [(2,3,4), (5,6,7), (8,9,10)]


print(list(zip(*x)))