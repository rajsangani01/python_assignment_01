# Write a Python program to check whether a list contains a sub list.


def check_substring(l):

    newlist = []
    for i in l:
        if type(i) == list:
            newlist.append(i)

    print(newlist)

check_substring([1,2,3,[4,5,6]])