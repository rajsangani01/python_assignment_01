'''fin = open("movies.txt","r")

str = fin.read()

words = str.split()

max_len = len(max(words, key=len))

for word in words:
    if len(word)==max_len:
        longest_word =word
        
print(longest_word)
'''
#file = open("series.txt" , "w")
file = open("series.txt" , "r")

# file.write("name : raj.")
# file.write("\nname : rajoo.")
# file.write("\nname : rajesh.")
# file.write("\nname : rajvi.")
# file.write("\nname : rajkot.")

string = file.read()
words = string.split()

max_len = len(max(words, key=len))

for word in words :
    if len(word) == max_len :

        longest_word = word
print(longest_word)



