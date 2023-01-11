# Differentiate between append () and extend () methods?

# Append() Merthod :
#       In append method single element is added mutiple times in your list at last index. 

# Example :

x = [1,2,3,4,5]
x.append(6)
x.append(7)
x.append(8)
x.append(9)
x.append(10)
print(x)

# Extend() Method :
        # In extend method you want add your other list items in your main list. first which list is you want to extend after use extend function,which list is you want to extend in other list.

# Example :

firstlist = [1,2,3,4,5]
secondlist = [6,7,8,9,10]
firstlist.extend(secondlist)
print(firstlist)