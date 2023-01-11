# How will you compare two lists?

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]

if list1 == list2 :
    print("list1 and list2 are same :")
else :
    print("list1 and list2 are not same :")

list1 = [10,20,30,40,50]
list2 = [20,30,40,50,10]
list3 = [60,70,100,90,80]

list1.sort()
list2.sort()
list3.sort()

if list1 != list2 :
    print("list1 and list2 not same :")
else :
    print("list1 and list2 same :")

if list1 != list3 :
    print("list1 and list3 not same :")
else:
    print("list1 and list3 same :")

if list2 == list3 :
    print("list2 and list3 same :")
else :
    print("list2 and list3 not same :")