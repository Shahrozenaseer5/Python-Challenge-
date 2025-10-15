 # 'Finally' keyword in python
# Finally code block is also a part of exception handling. When we handle exception using the try and except block, 
# We can include a finally block at the end. Finally block will always executed, so it i generally used for doing the concluding tasks like
# closing the resources or closing database connection or may be ending the program execution with a delightful message.
# Syntax :
# try :
# statements which could generate 
# exceptions
# except :
# solutiuon of generated exception
# finally :
# block of code which is going to execute in any situation

# finally block is executed irrespective of the outcome of try....except...else blocks.
# One of the important  use cases of finally block is in a function which returns a value.
# try : 
#   lst = [11,22,33,44,55,66]
#   i = int(input('enter the index : '))
#   print(lst[i])
# except :
#   print('invalid index')
# # finally :
# #   print('I am always executed')
# print('Done')

# Intrview quetion : why we need finally if we can use simple print statement to print output always?
# Answer : We can use print statement in simple programs but when we deal with functions or complex programs, we need need finally block 
# which will be executed whether function returns a value or not. if function returns any value, then print statement will never executed.
# On the other hand, finally block will always executed even if a function returns any value.
def func1() :
  try : 
   lst = [11,22,33,44,55,66,77]
   i = int(input('enter the index : '))
   print(lst[i])
   return 1
  except :
   print('invalid index')
   return 0
  finally :
   print('I am always executed')
 # here, if function return any value, finally block still executed. that's the reason why we use finally keyword in place of simple print statement.
 # print('Done')

x = func1()
print(x) # it will print 0 or 1 depending on the input that user enters.

# Note : Don't use same code outside and inside a function. That may cause unexpected output.
