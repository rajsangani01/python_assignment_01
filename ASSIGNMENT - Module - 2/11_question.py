# Write a python program to sum of the first n positive integers.

x = int(input("enter any no :"))
y = 0

for z in range(1,x+1) :
    y = z+y
    
print(y)