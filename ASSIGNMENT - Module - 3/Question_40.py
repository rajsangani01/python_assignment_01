# Write a Python script to merge two Python dictionaries

mydict = {
    "tata" : "harrier",
    "suzuki" : "alto"
}

newdict = {
    "tata" : "nexon",
    "volvo" : "xc90"
}

mydict.update(newdict)
print(mydict)