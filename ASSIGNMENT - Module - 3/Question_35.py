# Write a Python script to check if a given key already exists in a dictionary.

mydict = {
    "hyundai" : "creta",
    "suzuki" : "alto",
    "tata" : "harrier",
    "tata" : "harrier",
    "lexus" : "lx",
    "kia" : "seltos"
}

keys = input("enter keys :")

if keys in mydict.keys() :
    print("keys is already exists :")
else :
    print("ok keys is access :")