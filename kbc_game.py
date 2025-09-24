
# Kon Banega Karorpati

import sys

print('Fastest Finger First : ','
')
print('Arrange these Indian Prime Ministers in order of their first term in office: ')
print('A. Manmohan Singh')
print('B. Atal Bihari Vajpayee')
print('C. Jawahar Lal Nehru')
print('D. Indra Gandhi')

# Correct order: C → D → B → A
Correct_Answer = ['CDBA', 'cdba']
# print(type(Correct_Answer))
Answer = input('Enter your answer : ')
if Answer in Correct_Answer :
  print('You  are selected.')
else :
  print('Better luck next time 🙂')
  sys.exit()

# Now selected person will play KBC :
#  Money Ladder (with Safe Levels)

# Q1  Rs 1,000
# Q2  Rs 2,000
# Q3  Rs 3,000
# Q4  Rs 5,000
# Q5  Rs 10,000 (Safe Level 1)
# Q6  Rs 20,000
# Q7  Rs 40,000
# Q8  Rs 80,000
# Q9  Rs 1,60,000
# Q10 Rs 3,20,000 (Safe Level 2)
# Q11 Rs 6,40,000
# Q12 Rs 12,50,000
# Q13 Rs 25,00,000
# Q14 Rs 50,00,000
# Q15 Rs 1 Crore (Grand Prize)
# 👉 If contestant quits, they take current winnings.
# 👉 If they answer wrong, they fall back to the last safe level.

# Game Start :
# Q1  Rs 1,000
Question_1 = '1- What is the capital of Pakistan?'
options = ['A. Lahore','B. Islamabad', 'C. Karachi', 'D. Multan']
correctAnswer_1 = ['B. Islamabad','b. islamabad','b','B']
print(Question_1)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_1 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q2 – Rs 2,000
Question_2 = '2- Which planet is known as the “Red Planet”?'
options = ['A. Venus','B. Jupiter', 'C. Mars', 'D. Saturn']
correctAnswer_2 = ['C. Mars','c. mars','c','C']
print(Question_2)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_2 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q3 – Rs 3,000
Question_3 = '3- Who is known as the “Father of the Nation” in India?'
options = ['A. Subhas Chandra Bose','B. Jawaharlal Nehru', 'C. Mahatma Gandhi', 'D. Bhagat Singh']
correctAnswer_3 = ['C. Mahatma Gandhi','c. mahatma gandhi','c','C']
print(Question_3)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_3 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q4 – Rs 5,000
Question_4 = '4- Which is the largest mammal in the world?'
options = ['A. Elephant','B. Blue Whale', 'C. Giraffe', 'D. Hippopotamus']
correctAnswer_4 = ['B. Blue Whale','b. blue whale','b','B']
print(Question_4)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_4 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q5 – Rs 10,000 (Safe Level 1)
Question_5 = '5- The currency of Japan is?'
options = ['A. Yen','B. Won', 'C. Dollar', 'D. Peso']
correctAnswer_5 = ['A. Yen','a. yen','a','A']
print(Question_5)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_5 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q6 – Rs 20,000
Question_6 = '6- Who was the first person to walk on the moon?'
options = ['A. Yuri Gagarin','B. Buzz Aldrin', 'C. Neil Armstrong', 'D. Michael Collins']
correctAnswer_6 = ['C. Neil Armstrong','c. neil armstrong','c','C']
print(Question_6)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_6 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q7 – Rs 40,000
Question_7 = '7- Which of these is a prime number?'
options = ['A. 21','B. 23', 'C. 27', 'D. 35']
correctAnswer_7 = ['B. 23','b. 23','b','B']
print(Question_7)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_7 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q8 – Rs 80,000
Question_8 = '8- In computing, what does “CPU” stand for?'
options = ['A. Central Processing Unit','B. Computer Power Unit', 'C. Control Processing Utility', 'D. Central Power Unit']
correctAnswer_8 = ['A. Central Processing Unit','a. central processing unit','a','A']
print(Question_8)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_8 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q9 – Rs 1,60,000
Question_9 = '9- Who wrote the famous play Hamlet?'
options = ['A. William Shakespeare','B. Charles Dickens', 'C. Leo Tolstoy', 'D. Mark Twain']
correctAnswer_9 = ['A. William Shakespeare','a. william shakespeare','a','A']
print(Question_9)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_9 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q10 – Rs 3,20,000 (Safe Level 2)
Question_10 = '10- Which gas do plants absorb during photosynthesis?'
options = ['A. Oxygen','B. Nitrogen', 'C. Carbon Dioxide', 'D. Hydrogen']
correctAnswer_10 = ['C. Carbon Dioxide','c. carbon dioxide','c','C']
print(Question_10)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_10 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q11 – Rs 6,40,000
Question_11 = '11- In which year did Pakistan win its first Cricket World Cup?'
options = ['A. 1983','B. 1987', 'C. 1990', 'D. 1992']
correctAnswer_11 = ['D. 1992','d. 1992','d','D']
print(Question_11)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_11 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q12 – Rs 12,50,000
Question_12 = '12- The Great Wall of China was primarily built to protect against which group?'
options = ['A. Mongols','B. Romans', 'C. Persians', 'D. Japanese']
correctAnswer_12 = ['A. Mongols','a. mongols','a','A']
print(Question_12)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_12 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q13 – Rs 25,00,000
Question_13 = '13- Who painted the Mona Lisa?'
options = ['A. Pablo Picasso','B. Vincent Van Gogh', 'C. Leonardo da Vinci', 'D. Michelangelo']
correctAnswer_13 = ['C. Leonardo da Vinci','c. leonardo da vinci','c','C']
print(Question_13)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_13 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q14 – Rs 50,00,000
Question_14 = '14- The theory of relativity was proposed by which scientist?'
options = ['A. Isaac Newton','B. Nikola Tesla', 'C. Galileo Galilei', 'D. Albert Einstein']
correctAnswer_14 = ['D. Albert Einstein','d. albert einstein','d','D']
print(Question_14)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_14 :
  print('Correct Answer ! you can move forward to next question.', '
')
else :
  print('Wrong Answer !')
  sys.exit()
# Q15 – Rs 1 Crore (Grand Prize)
Question_15 = '15- What is the smallest prime number?'
options = ['A. 0','B. 1', 'C. 2', 'D. 3']
correctAnswer_15 = ['C. 2','c. 2','c','C']
print(Question_15)
for option in options :
  print(option)
answer = input('Enter your answer : ')
if answer in correctAnswer_15 :
  print('Mubarak ho! Aap ban gaye hain is season ke Crorepati! 🏆💰', '
')
else :
  print('Wrong Answer !')
  sys.exit()
