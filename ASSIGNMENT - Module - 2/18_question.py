#  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. if the string length of the given string is less than 3, leave it unchanged.

x = str(input("enter string :"))

if len(x) < 3 :
    print(x)

elif  x.endswith("ing") :
    print(x,end="")
    print("ly")

elif x[-3:-1] != "ing" :
    print(x,end="")
    print("ing")

else:
    print("nothing.")