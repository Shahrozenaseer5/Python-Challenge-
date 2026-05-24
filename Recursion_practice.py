
# Recursion in Python
# Recursion in Python means that a function calls itself in order to solve a problem.
# def factorial(n):
#   if n==0 or n==1:
#     print('factorial of n is : ', 1)
#     return 1
#   else :
#      res = n*factorial(n-1)
#      print('factorial of n is : ', res)
#      return res
# factorial(8)
# output will be :
#  factorial of n is :  1
# factorial of n is :  2
# factorial of n is :  6
# factorial of n is :  24
# factorial of n is :  120
# factorial of n is :  720
# factorial of n is :  5040
# factorial of n is :  40320
# 40320

# factorial(8) = 8*7*6*5*4*3*2*1 or factorial(8) = 8 * factorial(7)
# factorial(7) = 7*6*5*4*3*2*1      factorial(7) = 7 * factorial(6)
# factorial(6) = 6*5*4*3*2*1        factorial(6) = 6 * factorial(5)
# factorial(5) = 5*4*3*2*1          factorial(5) = 5 * factorial(4)
# factorial(4) = 4*3*2*1            factorial(4) = 4 * factorial(3)
# so we can say that :

# factorial(n) = n*factorial(n-1)


# if we want final answer for factorial(8) :
def factorial(n):
  if n==0 or n==1:
    return 1
  else :
    return n*factorial(n-1)
# Driver code :
print(factorial(8))
# it means : Recursion process works in this scenario as :
# 8*factorial(7)
# 8*7*factorial(6)
# 8*7*6*factorial(5)
# 8*7*6*5*factorial(4)
# 8*7*6*5*4*factorial(3)
# 8*7*6*5*4*3*factorial(2)
# 8*7*6*5*4*3*2*factorial(1)
# after this, 'if condition' will be 'True'. so we get 1 at last in recursion process.
# 8*7*6*5*4*3*2*1

# # Quick Quiz : Write a program to print Fibonacci Sequence
# # f(0) = 0
# # f(1) = 1
# # f(2) = f(1)+f(0)
# # f(n) = f(n-1)+f(n-2)
# # According to Fibonacci Sequence, we get :
# # 0,1,1,2,3,5,8,13...

# def fibonacci(n):
#   if n==0 :
#     return 0
#   elif n==1:
#     return 1
#   else :
#     return fibonacci(n-1)+fibonacci(n-2)

# # Driver code :
# print('Fibonacci sequence of 40 is : ',fibonacci(40))

# 1 - Sum of Natural Numbers
# Write a recursive function that returns the sum of first n natural numbers.
def sumOfNaturalNumbers(n):
  if n<=0: # 0 or negative numbers not allowed
    return 0
  elif n==1: # base case
    return 1
  else :
    return n+sumOfNaturalNumbers(n-1)

# Driver code :
n = int(input('Enter a number : '))
print('Sum of natural number n is : ' ,sumOfNaturalNumbers(n))

# 2 - Reverse a String
# Write a recursive function to reverse a string.
def reverseString(str):
  if len(str)==0: # base case
    return str
  else :
    return reverseString(str[1:])+str[0] # recursive case
# Recursion Tree
  #   reverse_string("python")
  #  → reverse_string("ython") + "p"
  #       → reverse_string("thon") + "y"
  #            → reverse_string("hon") + "t"
  #                 → reverse_string("on") + "h"
  #                      → reverse_string("n") + "o"
  #                           → reverse_string("") + "n"
  #                                → ""   (base case)
  # Now unwinding (bottom → up):
#   reverse_string("") = ""
# reverse_string("n") = "" + "n" = "n"
# reverse_string("on") = "n" + "o" = "no"
# reverse_string("hon") = "no" + "h" = "noh"
# reverse_string("thon") = "noh" + "t" = "noht"
# reverse_string("ython") = "noht" + "y" = "nohty"
# reverse_string("python") = "nohty" + "p" = "nohtyp"

str = input('Enter a string : ')
print('Reverse of string is : ',reverseString(str))

# 3 - Palindrome Check
# Write a recursive function to check if a string is a palindrome.

# Examples of Palindromes:
# Words:
# "madam" → same forward and backward
# "racecar"
# "level"
# Numbers:
# 121
# 1331
# 12321

def palindromeCheck(s):
  if len(s)<=1: # base case: 1 or 0 letters left
    return True
  elif len(s)>1 and s[0]==s[-1]: # check first and last character
     return palindromeCheck(s[1:-1]) # recursive step: shrink string
  else :
    return False

s = input('enter string : ')
print(palindromeCheck(s))
# Example Run: "madam"
# s = "madam"
# First = "m", Last = "m" → same → call palindromeCheck("ada")
# s = "ada"
# First = "a", Last = "a" → same → call palindromeCheck("d")
# s = "d"
# Length = 1 → returns True
# So the final result = True ✅

# 4. Power of a Number
# Write a recursive function to calculate a^b (a raised to the power b).
def power(a,b):
  if b == 0: # base case for power
    return 1
  elif b < 0: # handle negative exponent
    return 1 / power(a, -b)
  else :
    return a * power(a, b-1) # recursive step

a = int(input('Enter a number of a : '))
b = int(input('Enter a number of b : '))
print(power(a,b))
