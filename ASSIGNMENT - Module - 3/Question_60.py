# Write a Python program to read a random line from a file.


import random

myfl = open('myfile.txt', 'r')

# # myfl.write('name : raj sangani\nsubject : python\n')
# myfl.write('name : ravi patel\nsubject : java\n')
# myfl.write('name : neel mungra\nsubject : c++\n')
# myfl.write('name : ketan shah\nsubject : ui-ux\n')
# myfl.write('name : mukesh rajani\nsubject : golang\n')



print(random.choice(myfl.readlines()))

