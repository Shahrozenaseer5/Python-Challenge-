"""
Author      : Shahroze
Project     : Map, Filter, Reduce Examples in Python
Description : Demonstrates the use of higher-order functions: map(), filter(), and reduce().
              Includes exercises to practice these functions with lists.
Date        : 2025-11-14
"""

"""
In python, map, filter and reduce are build-in functions that allows you to apply a function to a sequence of elements
and return a new sequence. These functions are known as higher order functions, as they take other functions as arguments.

map() : 
map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
map function has the following arguments :
                       map(function, iterable)
The function argument is a function that is applied to each element in the iterable argument. iterable argument can be 
a list, tuple or any other iterable object.
"""
import os 
os.system('cls')
# Example of map function :
def cube(x) :
    return x*x*x
print(cube(5))

l = [1, 4, 22, 91, 33, 54]
# if we want to get a new list in which we can see cube of each element in list :
# newl = []
# for item in l : 
#   newl.append(cube(item))
# print(newl)

# we can do same thing by using map function :
# newl = list(map(cube , l))
# we can do same thing using lambda function
newl = map(lambda x : x*x*x , l)
# then we need to convert it into a list by using 'list' keyword
newl = list(map(lambda x : x*x*x , l))
print(newl)

# map() transforms data.


"""
filter() :
filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value)
and return a new sequence containing only the elements that meet the predicate. filter function has the following syntax :
                        filter(predicate , iterable)
predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument.
iterable argument can be a list, tuple or any other iterable object
"""
lst = [2,4,6,8,10,12,14,16,18,20]
# def filter_function(a) :
#     return a > 10
# newlst = filter(filter_function , lst)
# by using lambda function
newlst = list(filter(lambda a : a > 10 , lst)) # it will filter items in lst and give those values that are greater than 10.
print(newlst) # result will be same.
# filter() selects data.

# The filter() function applies a given function (that returns True or False) to each element of an iterable
# and keeps only the elements for which the function returns True.

"""
reduce() :
reduce function is a higher order function that applies a function to a sequence and returns a single value. 
It is a part of functool module in python and has the following syntax :
                              reduce(function, iterable)
function argument is a function that takes in two arguments and returns a single value.
iterable argument will be a sequence of iterable objects like list, tuple etc.
The  reduce function applies the function to the first two elements in the iterable and then applies the function to the result.
and the next element and so on. reduce function returns the final result.
"""
from functools import reduce
# list of numbers
lst_1 = [190,387,534,298,46,6]
# lst_1 = [577, 534, 298, 46, 6] sum of 190 and 387
# lst_1 = [1111, 298, 46, 6] sum of 577 and 534
# lst_1 = [1409, 46, 6] sum of 1111 and 298
# lst_1 = [1455, 6] sum of 1409 and 46
# lst_1 = [1461] sum of 1455 and 6
# that's how reduce function works
# calculate sum of the numbers using reduce function
sum = reduce(lambda x, y : x +  y , lst_1)
print(sum)

# Exercise 1 : Square Even Numbers (map + filter)
# Given a list of numbers, first filter only the even numbers, then square them.
nums = [1, 2, 3, 4, 5, 6]
newlist = list(filter(lambda x : x%2 == 0 , nums))
print(newlist)
square_newlist = list(map(lambda x : x*x , newlist))
print(square_newlist)

# Exercise 2 : Filter Names Starting With “A”
# Use filter() to keep only names that start with the letter A.
names = ["Ali", "Shahroze", "Ahsan", "Kamran", "Asad", "Bilal"]
names_A = list((filter(lambda A :  A.startswith('A')  , names)))
print(names_A)

# Exercise 3 : Convert Temperatures (map)
# Convert a list of temperatures from Celsius to Fahrenheit using this formula:
# F = C * 9/5 + 32
temps = [0, 10, 20, 30, 40]
new_temp = list(map(lambda C : int( C * 9/5 + 32 ) , temps))
print(new_temp)

# Exercise 4 : Multiply All Numbers (reduce)
# Use reduce() to calculate the product of all numbers.
from functools import reduce
nums = [2, 3, 4, 5]
multiple_nums = reduce(lambda c, d : c * d , nums)
print(multiple_nums)

# Exercise 5 : Count Odd Numbers (filter + reduce)
# Filter out odd numbers, then use reduce() to count how many remain.
nums = [1, 3, 4, 6, 7, 9, 10, 12]
odd_nums = list(filter(lambda y : y%2 != 0 , nums))
print(odd_nums)
from functools import reduce 
count_oddNumbers = reduce(lambda acc, x: acc + 1 if x % 2 != 0 else acc, nums, 0)
"""
acc → the running total (starts at 0 because of the last argument of reduce)
x → each element of the list as reduce() iterates
acc + 1 if x % 2 != 0 else acc → if the current element is odd, add 1 to the accumulator, otherwise keep it the same
So acc accumulates the count as the function goes through the list.

Think of it like a basket that collects a value while you walk through all the items.
"""
print(count_oddNumbers)
