# How do you perform pattern matching in Python? Explain.

# raj99@gmail.com

import re

mail = input("enter mail :")
mail_pattern = "[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"

y = re.findall(mail_pattern,mail)

if y :
    print("access :")
else :
    print("not access :")