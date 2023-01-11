# Write a Python program to reverse a tuple.



def reversed(tuples) :
    newtuple = tuples[::-1]
    return newtuple

tuples = ("a","b","c","d","e","f")
print(reversed(tuples))