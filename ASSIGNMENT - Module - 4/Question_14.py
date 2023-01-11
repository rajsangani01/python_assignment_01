# Write python program that user to enter only odd numbers, else will raise an exception.


user = int(input('enter odd nums :'))

try:
    if user%2 != 0:
        print('odd')
    else:
        print('even')
except:
    print('ok')