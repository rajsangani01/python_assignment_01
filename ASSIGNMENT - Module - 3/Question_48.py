# Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. Sample string:
# 'w3resource'
# o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


def count_words(s):
    new_dict = {}

    for i in s:

        new_dict[i] = s.count(i)
        

    print(new_dict)

count_words('rajsangani')


'''d = {}
name = 'rajsangani'
for i in name:
    d[i] = name.count(i)

print(d)'''

