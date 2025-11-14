import os 
os.system('cls')
"""
is and == are used for comparison, but they do very different things:
== (Equality) :
What it does: Checks if the values of two objects are the same.
Example:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, because the lists have the same contents

Even though a and b are two different lists in memory, == compares the contents.

is (Identity) :

What it does: Checks if two variables point to the exact same object in memory.

Example:

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # False, because a and b are different objects in memory
print(a is c)  # True, because c references the same object as a

Summary : is and == both are comparison operators. 'is' compare exact location of object in memory but '==' compare values of two objects.
"""
# a = 33
# b = '33'
# print(a is b) # exact location in memory
# print(a == b) # values

a = [1, 2, 4, 100]
b = [1, 2, 4, 100]
# python will make 2 lists separately
print(a is b) # False because a and b stored separately in memory
print(a == b) # True because values of a and b are comparatively equal
# Analogy : assume 2 people buy iphone 14 from apple. Here,  2 phones given to 2 different people (just like object in memory)
#  but yeah features (like values of 2 objects) are same in both phones.
 
# Dealing with integers, strings, tuples etc :
c = 3
d = 3
print('\n', c is d)
print(c == d)
# In this case, both is and == shows True because constant (3) is stored once in memory and values of c and d are same.
print('\n')

e = 'Shahroze'
f = 'Shahroze'
print(e is f)
print(e == f)
# This will also show True in both comparisons.
print('\n')
g = (2,4,6)
h = (2,4,6)
print(g is h)
print(g == h)
# Results will be True because tuples are immutable.
print('\n')
# with 'None'
i = None
j = None
print(i is j)
print(i is None)
print(i == j)
print('\n')
# Exercise 1 : Lists
x = [10, 20]
y = [10, 20]
print(x is y) # False
print(x == y) # True

print('\n')
# Exercise 2 : Strings
a = "hello"
b = "hello"
# Try to explain why the result is what it is
print(a is b)
print(a == b)
# both is and == show True because in both a and b string identity is same so it will store once in python also thier values are same.
print('\n')
# Exercise 3 : integers
m = int("300")
n = int("300")
print(m is n) # Now this will be False
print(m == n) # Still True

# Here, int("300") creates a new object each time, so is will reliably show False.

