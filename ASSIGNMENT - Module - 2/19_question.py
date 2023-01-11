# Write a Python program to find the first appearance of the substring 'not' and 'poor' from given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.

'''x = "raj is not that type of poor"
y = "raj is poor"

print(x.replace("not that type of poor","good"))
#print(x)
print(y)
'''
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
