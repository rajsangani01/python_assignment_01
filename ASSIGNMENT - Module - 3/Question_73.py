# Write a Python function that checks whether a passed string is palindrome
# or not


def palindrome_str(s):

    if s == s[::-1]:
        print('palindrome string :')
    else:
        print('Not palindrome')

palindrome_str('pip')
