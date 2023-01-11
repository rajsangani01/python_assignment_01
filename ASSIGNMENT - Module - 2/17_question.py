# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

'''def characters(a, b):
  new_a = b[:2] + a[2]
  new_b = a[:2] + b[2]

  return new_a +' ' + new_b
print(characters('abc', 'xyz'))'''




def fun2(s1, s2):
  new_s1 = s2[:2] + s1[2]
  new_s2 = s1[:2] + s2[2]

  return new_s1 + ' ' + new_s2

print(fun2('abc', 'xyz'))
