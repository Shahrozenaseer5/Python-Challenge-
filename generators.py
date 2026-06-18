"""
========================================================================
Project       : Generators in Python - Concepts & Exercises
Author        : Shahroze
Date          : 2026-03-25
Description   : 
    This Python file demonstrates the use of generators in multiple contexts:
    1. Basic generator functions and generator expressions
    2. Converting lists to generators for memory-efficient iteration
    3. File-like streaming with generators
    4. Infinite generators (even numbers)
    5. Memory comparison between lists and generators
    6. Chaining generators to form pipelines
Purpose       : 
    - Learn and practice lazy evaluation
    - Understand memory efficiency of generators
    - Explore real-world applications like file streaming and pipelines
Python Version: 3.x
========================================================================
"""
"""
Generrators in python : 
                       A generator is a function that returns values one by one (lazily) instead of returning everything at once.
                       It uses 'yield' instead of 'return'.

Real-life analogy :
=> Think of a water tap vs water tank:
=> List = water tank
=> You fill the whole tank first → takes space → then use water.
=> Generator = tap
=> Water comes only when you open it → no storage → just flow.

👉 Generators don’t store everything → they produce on demand.

Why we use generators?
=> Main reason: memory efficiency + performance

- No need to store large data in memory
- Faster for large datasets
- Works well with streams (files, APIs, logs)

How to use generators?

1. Generator function (yield)
def squares(n):
    for i in range(n):
        yield i * i

2. Generator expression (like list comprehension)
gen = (i*i for i in range(5))

Generator vs List (behavior difference) : 
List :
lst = [i*i for i in range(5)]
print(lst)

Output : [0, 1, 4, 9, 16]

- Stores ALL values in memory
- Can access anytime
- Faster for small data

Generator : 
gen = (i*i for i in range(5))
print(gen)

Output : <generator object ...>

To get values:

              for val in gen:
                 print(val)
- Does NOT store values
- Gives one value at a time
- Can be used only once (gets exhausted)

Key differences :
Feature           	        List	          Generator
Memory	                    High	          Very low
Execution	                Immediate	      Lazy (on demand)
Speed (for small dataset)	Faster	          Slightly slower
Reusability	                Yes	              No (once used)

When to use generators :

=> Use generators when:

1. Large data processing

def read_file(file):
    for line in file:
        yield line

=> Reads file line by line (not full file in memory)

2. Infinite sequences

def infinite_numbers():
    i = 1
    while True:
        yield i
        i += 1
3. Data pipelines

gen = (x*x for x in range(1000000000))

=> No memory crash

When generators prevent memory issues :
Problem (list):
lst = [i for i in range(10**8)]  # huge memory usage
Solution (generator):
gen = (i for i in range(10**8))  # almost no memory

=> Only one value exists at a time → no memory overflow

Mental model :
- If you need all data at once → use list
- If you need data one by one → use generator
"""
# Generators 
def my_generator() :
  for i in range(59999999) :
    # complex computations
     yield i   # we use yield instead of return due to get values on demand

gen = my_generator()
# print(next(gen)) # we use next for getting next value from generator
# print(next(gen))
# print(next(gen))

# another way to use generators :
for j in gen :
  print(j)

"""
Exercise 1 : Convert List → Generator (core habit)
Task:
- You already know this:
lst = [i*i for i in range(10)]
=> Convert it into a generator and:
=> Print first 3 values using next()
=> Then print remaining values using a loop
Goal:
- Understand lazy execution
- See how generator gets exhausted step by step
"""
def square(n) : 
  for a in range(n) :
    yield a * a

# my_square = (i*i for i in range(10))
my_square = square(10)
print(next(my_square))
print(next(my_square))
print(next(my_square))

for b in my_square :
  print(b)

for b in my_square :
  print(b)
# “A generator produces each value only once and does not store it. that's why second for loop for b prints nothing”.
# - Generator = stream, not storage
# - Once the stream flows past a point, you can’t go back

"""
Exercise 2 : File-like Streaming (real-world use)
Task:
=> Create a generator that simulates reading data line by line.
data = ["line1", "line2", "line3", "line4", "line5"]

Write a generator:

def read_data(data):
    # yield one line at a time

Then:
=> Loop through it and print lines
=> Try calling it again (observe behavior)
Goal:
- Understand one-time use
- Mimics real-world: file reading, APIs
"""
def read_data(data) :
  for line in data :
    yield line

data = [
    "Line 1 : The sun rises in the east.",
    "Line 2 : Birds start singing in the morning.",
    "Line 3 : Dew drops sparkle on the grass.",
    "Line 4 : Children walk to school happily.",
    "Line 5 : Morning breeze feels fresh and cool.",
    "Line 6 : Street vendors start setting up their stalls.",
    "Line 7 : Coffee aroma fills the neighborhood.",
    "Line 8 : Roads begin to fill with vehicles.",
    "Line 9 : People greet each other with smiles.",
    "Line 10 : The day officially begins with energy."
]

gen = read_data(data)
print(next(gen))
print(next(gen))

for line in gen :
  print(line)

for line in gen :
  print(line)
# “A generator produces each value only once and does not store it. that's why second for loop for line prints nothing”.
# If we want to reuse generator, we need to create it again.

"""
Exercise 3 : Infinite Generator (important concept)
Task:
=> Create a generator that produces even numbers infinitely

Example output:
2, 4, 6, 8, 10...

Then:
=> Print only first 10 values using next()
Goal:
- Understand infinite streams
- Learn control (you decide when to stop, not the generator)
"""
def even_numbers() :
  n = 2
  while True :
    yield n
    n = n + 2

my_gen =  even_numbers()
# for a in my_gen :
#   print(a)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

"""
Exercise 4 : Memory Comparison (real understanding)
Task:
Create:
A list:
lst = [i for i in range(1000000)]
A generator:
gen = (i for i in range(1000000))

Use :

import sys
print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
Goal:
Actually see memory difference
This is where generators “click” deeply

Bonus :
Create a pipeline:

- nums = (i for i in range(10))          # generator 1
- squares = (i*i for i in nums)          # generator 2
- even_squares = (i for i in squares if i % 2 == 0)

=> Print results

Goal:
- Understand chaining generators
- This is how real ML/data pipelines work
"""
import sys
lst = [i for i in range(1000000)]

def num() :
  for x in range(1000000) :
    yield x * x

gen = num()
print("Size of List : ", sys.getsizeof(lst), 'bytes')
print("Size of generator : ", sys.getsizeof(gen), 'bytes')

def generator_1() :
  for i in range(10):
    yield i

def generator_2() :
  for j in generator_1() :
    yield j * j

def generator_3() :
  for k in generator_2() :
    if k % 2 == 0 :
      yield k
print('Generator 1 : ')
gen_1 = generator_1()
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print('Generator 2 : ')
gen_2 = generator_2()
print(next(gen_2))
print(next(gen_2))
print(next(gen_2))
print('Generator 3 : ')
gen_3 = generator_3()
print(next(gen_3))
print(next(gen_3))
print(next(gen_3))
# This is called generator pipelines — common in real data processing (big files, streams, ML pipelines).