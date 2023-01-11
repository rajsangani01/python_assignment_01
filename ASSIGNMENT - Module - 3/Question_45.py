# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
#  Sample data: {'1': ['a','b'], '2': ['c','d']}
#  Expected Output:
#  ac ad bc bd

dicts = {'1': ['a','b'],'2': ['c','d']}

dicts['1'],dicts['2'] = ["a","b"],["c","d"]

print(dicts)