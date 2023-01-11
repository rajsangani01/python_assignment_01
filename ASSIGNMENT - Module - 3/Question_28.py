# Write a Python program to find the repeated items of a tuple.

'''x = (1,2,3,4,1,2,3,3,2,2,2,1,1,1,1,1)

for y in x :
    if x.count(y) > 1 :
        print(y)'''


x = (1,2,3,4,5,1,2,6,7,8,8,9)


for i in x:
    if x.count(i) > 1:
        print(i)
        