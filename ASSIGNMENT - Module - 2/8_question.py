# Write a Python program to test whether a passed letter is a vowel or not.

def fun(str):
    vowel =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if str in vowel:
        print ("It is a vowel")
   
    else:
        print ("it is not vowel")

fun("r")