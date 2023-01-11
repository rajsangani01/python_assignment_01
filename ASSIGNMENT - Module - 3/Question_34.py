# Write a Python script to concatenate following dictionaries to create a new one.

'''mydict = {
    "hyundai" : "creta",
    "suzuki" : "alto",
    "tata" : "harrier"
}

newdict = {
    "food" : "chinese",
    "travel" : "leh-ladakh",
    "bike" : "royal-enfield"
}

mydict.update(newdict)
print(mydict)'''


d1 = {1:2, 3:4}
d2 = {5:6, 7:8}
d3 = {9:10, 11:12}
d4 = {}

for d in (d1, d2, d3):
    d4.update(d)

print(d4)