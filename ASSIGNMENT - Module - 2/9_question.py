# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.

x = int(input('enter first num :'))
y = int(input('enter second num :'))
z = int(input('enter third num :'))



if x==y or y==z or z==x:
    print('sum : 0')
else:
    print(x+y+z)