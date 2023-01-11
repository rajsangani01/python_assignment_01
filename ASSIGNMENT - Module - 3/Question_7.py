# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

x = str(input("enter strings :"))

print("length of string :",end=" ")
print(len(x))
# print(x)

if len(x) > 2 :
    print(x[0:2] + x[-2:])
else:
    print("length of given string is short :")


if x[0:1] == x[-1:] :
    print(x[0] + x[-1])
    print()
else:
    print("first and last characters of given string is not same :")

