# How Do You Traverse Through A Dictionary Object In Python?

mydict = {
    "hyundai" : "creta",
    "suzuki" : "alto",
    "tata" : "harrier",
    "tata" : "harrier",
    "lexus" : "lx",
    "kia" : "seltos"
}


# using key method :

for key in mydict.keys():
    print(key)

# using values method :

for value in mydict.values():
    print(value)


# using items method :

for item in mydict.items():

    print(mydict)