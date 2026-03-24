"""
===============================================================================
File Name   : function_caching_examples.py
Author      : Shahroze
Date        : 2026-03-24
Description : Demonstrates Python function caching using functools.lru_cache and memoization. Includes examples for:
- Fibonacci sequence
- Factorial
- Basic timing test with simulated delay
- Limited cache size and LRU behavior
- Cache info tracking
              
Purpose : 
1. Understand how @lru_cache stores function results in memory.
2. Learn when and why caching improves performance.
3. Observe cache hits, misses, and LRU eviction behavior.
4. Compare execution time with and without caching.
              
Notes :
- Cache is maintained only during the program run. Restarting the program clears the cache.
- Use caching primarily for functions with repeated or expensive computations.
- maxsize parameter controls cache size and LRU eviction policy.
===============================================================================
"""
"""
" Function caching " in Python is a way to store the results of expensive or frequently called functions so that repeated calls
with the same arguments return the cached result instead of recalculating. It improves performance, especially for
recursive functions or functions with heavy computations.

Why we need it ?
- Avoids redundant computations.
- Speeds up programs.
- Reduces resource usage (CPU, memory, time).

How to use it :
Python provides functools.lru_cache:

from functools import lru_cache

@lru_cache(maxsize=None)  # None means unlimited cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))  # Uses cached results for faster calculation
- @lru_cache automatically remembers previous results.
- maxsize controls how many results are cached (Least Recently Used is removed when full).

Memoization :
Memoization is a software optimization technique that speeds up programs by caching the results of expensive function calls
and returning the cached result when the same inputs occur again. It is a specific form of caching, often used in dynamic programming
and recursion to avoid redundant calculations, significantly reducing time complexity.
"""
import os
import time
import functools
from functools import lru_cache
@lru_cache(maxsize = None) # None means unlimited cache
def fibonacci(n) :
  if n<2 :       # base case
    return n
  return fibonacci(n-1) + fibonacci(n-2)     # function calls itself
print(fibonacci(35))    # Uses cached results for faster calculation
# 2nd example
@lru_cache(maxsize = None)
def fx(n) :
  time.sleep(4)
  return n*2

print(fx(30))
print('Done for 30')
print(fx(20))
print('Done for 20')
print(fx(10))
print('Done for 10')

print(fx(30))
print('Done for 30')
print(fx(20))
print('Done for 20')
print(fx(10))
print('Done for 10')
print(fx(60))       # this computation again take 4 seconds to run
print('Done for 60')
""" This program uses @lru_cache from functools module which is used to store results of computations in function cache
and when same values comes again, it will show results directly from cache without doing computations. This technique 
called memoization. """

"""
Important Note : 
                Cache will mentained in 1 program run only and if we restart that program it will take exactly same time.
- functools.lru_cache (or any standard function caching in Python) only exists in memory while the program is running.
- Once we restart the program, the cache is cleared, so the function will recompute everything from scratch.
"""

"""
When to use @lru_cache ?
- Use @lru_cache when computations are limited and chances occur when same values repeat. 
- Use @lru_cache when program takes too much time to compute.

                                    BUT
- Don't use @lru_cache when thier is no chance of repeatition of values.
- Don't use @lru_cache when program is simple.
"""
# Exercise 1 : Basic Timing Test 
# - Create a function that sleeps for 2 seconds and returns n + 10
# - Call it twice with same value
# - First call should be slow, second should be instant using cache
@lru_cache(maxsize = None)
def plus(n) :
  time.sleep(2)
  return n+10
start = time.time()
print(plus(77))   # First call (slow)
print("Time:", time.time() - start)

start = time.time()
print(plus(77))   # Second call (fast - cached)
print("Time:", time.time() - start)

# Exercise 2 : Factorial with Cache
# - Write a recursive factorial function
# - Apply @lru_cache
# - Compare speed with and without cache
def factorial(n) :
  if n == 0 :
    return 1
  return n* factorial(n-1)
start = time.time()
print(factorial(15))
end = time.time()
print("Factorial without @lru_cache Time:", end - start)

@lru_cache(maxsize = None)
def factorial_cached(n) :
  if n == 0 :
    return 1
  return n * factorial_cached(n-1)
start = time.time()
print(factorial_cached(15))
print(factorial_cached(15))
end = time.time()
print("Factorial with @lru_cache Time:", end - start)

# Exercise 3 : Limited Cache Size
# Use @lru_cache(maxsize=3)
# Call function with values: 1,2,3,4,1,2,5
# Observe which values get recomputed
@lru_cache(maxsize = 3)
def Limited_cache(n) :
  time.sleep(3)
  return n + 10
print(Limited_cache(1))
print(Limited_cache(2))
print(Limited_cache(3))
print(Limited_cache(4))
print(Limited_cache(1))    # This should be FAST now
print(Limited_cache(2))
print(Limited_cache(5))

# Explanation :
# 1- Limited_cache(1) → ⏳ (3 sec)        Cache: [1]
# 2- Limited_cache(2) → ⏳ (3 sec)        Cache: [1, 2]
# 3- Limited_cache(3) → ⏳ (3 sec)        Cache: [1, 2, 3] (FULL)
# 4- Limited_cache(4) → ⏳ (3 sec)        Cache: [2, 3, 4]  (Removed 1)
# 5- Limited_cache(1) → ⏳ (3 sec)        Cache: [3, 4, 1]  (Removed 2)
# 6- Limited_cache(2) → ⏳ (3 sec)        Cache: [4, 1, 2]  (Removed 3)
# 7- Limited_cache(5) → ⏳ (3 sec)        Cache: [1, 2, 5]  (Removed 4)

# Exercise 4 : Cache Info Tracking
# - Use .cache_info() method
# Example:
# print(fib.cache_info())
# Track:
# - hits
# - misses
# - Run function multiple times and observe changes

@lru_cache(maxsize=None)
def fib(n) :
  if n<2 :
    return n
  return fib(n-1) + fib(n-2)
print(fib(10))
print(fib.cache_info())

""" 
Explanation:

hits=9 → these are repeated calls that were returned from cache
misses=11 → the first time each value from 0 to 10 was computed
maxsize=None → unlimited cache
currsize=11 → cache contains values 0 through 10
"""