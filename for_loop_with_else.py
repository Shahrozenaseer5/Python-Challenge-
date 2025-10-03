
# for loop with else in python
# python allows the else keyword to be used with for and while loop too.
# else block appears after the body of the loop.
# the statement in else block will be executed after all iterations are completed.
# the program exits the loop only after the else block is executed.

# basic syntax : 
                # for counter in sequence :
                  # statements inside for loop block
                # else :
                  # statements inside else block
for i in range(5) :
  print(i)
else :
  print('Sorry ! no i found')
# Conclusion : if control can't go into for loop then else block will be executed

for i in [] :
  print(i)
else :
  print('Sorry ! no i found')
# in this case, only else block will be executed because list have no items in it

for i in range(6) :
  print(i)
  if i == 4 :
    break
else :
  print('Sorry ! no i found')
# in this case, The else block only runs if the loop finishes normally, meaning it wasn’t terminated by a break.
# If the loop ends because of a break, the else block is skipped.

i=0
while i<7 :
  print(i)
  i = i+1
  # if i == 4:
  #   break
else :
  print('Sorry ! no i found')

for x in range(5) :
  print('iteration number {} in for loop '.format(x+1))
else :
  print('else blok')
print('out of loop')
# {} → placeholder in a string.
# .format(value) → replaces {} with that value.

for x in range(5):
    print(f'iteration number {x+1} in for loop') # with f-strings
else :
  print('else blok')
