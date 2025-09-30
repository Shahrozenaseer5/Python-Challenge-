
# sets in python
# Basic definition : Set is a collection of well defined objects
# A set in Python is an unordered collection of unique and immutable data items.
# Python's set type is a built-in data structure with several defining characteristics:
# Unordered: 
#           Items in a set don't have a defined order, meaning they cannot be accessed by an index like lists or tuples.
# The order may change when the set is modified or printed.
# Unique Elements:
#                 Sets automatically enforce that every element within them is unique. 
# If you try to add a duplicate element, it will be ignored, and the set will remain unchanged.
# Mutable:
#         The set itself is mutable, meaning you can add or remove elements after it's created.
# Immutable Elements: 
#                    The elements (the items inside the set) must be hashable (immutable).
# This means you can have numbers, strings, or tuples in a set, but not mutable types like lists or other sets.
# set is created within curly brackets {}
# sets are unchangeable, meaning you can't change items of the set once created. sets don't contain duplicate values.
s = {2,3,4,5,3,4} # set ignore duplicate values
print(s)
# set can contain different types of values
info = {'Corola', 19, True, 33.83, 19}
print(info) 
# order is not guaranteed in sets. That's why we can't access them through index as we access in lists,tuple,strings etc

# Now we are going to create an empty set
# shah = {} output will be dictionary and this is wrong because syntax of dictionaries and sets is same
# so we use set() function for creating empty set
shah = set()
print(type(shah))

res = {22, "Ahmad", 33.76, 22, False}
# Now we can access set items with the help of for loop
for items in res:
  print(items)
