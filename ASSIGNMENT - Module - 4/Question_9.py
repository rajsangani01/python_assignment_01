# Write a Python program to write a list to a file.

l = ['raj', 'neel', 'nitin', 'lakshman']
myfl = open('myfile.txt', 'w')

myfl.write(str(l))

