# Write a Python program to calculate the area of a trapezoid.


# formula : (a+b/2)*h
# a = base 1
# b = base 2
# h = height


base_1 = 5
base_2 = 6
height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)