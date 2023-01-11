# Write a Python program to read last n lines of a file.

myfl = open("file.txt" , "r")
print(myfl.readlines()[-1])