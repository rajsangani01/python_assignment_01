# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length islessthan 2,return instead of the empty string.
# Sample String:w3resource'
# Expected Result: 'w3ce'
# Sample String: 'w3'
# Expected Result: 'w3w3'
# Sample String: ' w'
# Expected Result: Empty String



def get_string(string0):

    if len(string0) > 1 :
        return string0[:2] + string0[-2:]

    else:
        print("Empty String :")



string_input=str(input("Enter String :"))

print(get_string(string_input))