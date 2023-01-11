# Write a Python function that takes a list of words and returns the length of the longest one.

def find_longest_word(words_list):
    word_len = []
    
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    # print(word_len)
    return word_len[-1][0] , word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))

# result = find_longest_word(["PHP", "Exercises", "Backend"])
# print("\nLongest word: ",result[1])
# print("Length of the longest word: ",result[0])



def func1(l):

    new_list = []

    for i in l:
        new_list.append((len(i), i))

    new_list.sort()
    return new_list[-1][0], new_list[-1][1]


print(func1(['abc', 'abca']))
