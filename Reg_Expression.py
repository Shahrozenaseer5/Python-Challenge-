"""
===============================================================================
Project       : Python Regular Expressions (Regex) Exercises
Author        : Shahroze
Date          : 2026-04-05
Language      : Python 3.x
Purpose :
A comprehensive collection of regex exercises to practice and master
Regular Expressions in Python. This file demonstrates:
- Pattern matching
- Text searching and extraction
- Data cleaning
- Practical real-world examples

Contents :
1. Basic regex search and match
2. Email extraction
3. Words ending with "ing"
4. Removing punctuation from text
5. Extracting proper names (capitalized words)
6. Extracting valid Pakistani phone numbers
7. Bonus exercises for practice

Key Concepts :
- Meta characters: ., ^, $, \d, \w, \s, etc.
- Quantifiers: *, +, ?, {n}, {n,}, {n,m}
- Character classes: [abc], [^abc], [a-z], etc.
- Grouping & lookarounds
- Special sequences: \b, \B, \d, \w
- re module functions: re.search(), re.findall(), re.sub(), re.finditer()

References :
- Python Regex Docs: https://docs.python.org/3/library/re.html
- Regexr: https://regexr.com/
- IBM Regex Reference: https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

Usage :
- Each section is an independent exercise with explanations.
- Run the script to see outputs of various regex patterns.
- Modify 'text' and 'pattern' to test new scenarios.
===============================================================================
"""
"""
Regular Expression :
                    A regular expression (regex) in Python is a pattern used to search, match, and manipulate text.
- Think of it like a smart “search formula” that lets you find specific patterns instead of
exact words.

- For applying regular expression, We use built-in module : import re
- Instead of checking text manually, you describe a rule, and Python finds everything that follows that rule.

❓ Why do we need it?
- Because real-world data is messy and unstructured.

Without regex:
- You write long loops
- Multiple if conditions
- Complex logic
With regex:
- One pattern can do everything cleanly

💡 Real situations where regex helps :
- Extract phone numbers from text
- Validate emails during signup
- Clean datasets before ML
- Search logs/files quickly
- Replace unwanted patterns

How to use it in Python :
Step 1: Import module
import re
Step 2: Use a pattern
import re
text = "My number is 12345"
result = re.findall(r"\d+", text)
print(result)

Output:
['12345']
Step 3: Common functions
re.search() → first match
re.findall() → all matches
re.sub() → replace text

Analogy 1 — “Metal Detector”

Imagine you are on a beach with a metal detector.

The beach = your text
Metal detector = regex
Gold = the pattern you want

You don’t check every grain of sand manually.
You just define what “metal” looks like, and the detector finds it.

Analogy 2 — “Hiring Filter”

- Imagine you are hiring people.
- Instead of reading every CV manually, you set rules:
- Must have “Python”
- Must have “2+ years experience”
Now only relevant candidates come to you.
- Regex is that filter system for text

It picks only what matches your criteria.

Final Understanding :
- Regex is not just a tool
- It’s a language to describe patterns in text

Once we get comfortable:
- we will stop thinking in loops
- we will start thinking in patterns

There are 3 things used in regular expression :
- pattern
- text
- match

=> Complete List of Regex Meta Characters
Meta characters are like:
                         grammar rules of regex language
🔤 1. Basic Meta Characters
Character	Meaning
.	        Any character except newline
^	        Start of string
$	        End of string
🔢 2. Character Classes
Character	Meaning
\d	        Digit (0–9)
\D	        Not a digit
\w	        Word character (a-z, A-Z, 0-9, _)
\W	        Not a word character
\s	        Whitespace (space, tab)
\S	        Not whitespace
🔁 3. Quantifiers (Repetition)
Character	Meaning
*	        0 or more times
+	        1 or more times
?	        0 or 1 time
{n}	        Exactly n times
{n,}	    n or more times
{n,m}	    Between n and m times
🎯 4. Character Sets
Character	Meaning
[abc]	    a OR b OR c
[^abc]	    NOT a, b, or c
[a-z]	    Range (a to z)
[A-Z]	    Uppercase letters
[0-9]	    Digits
🔗 5. Grouping & Combining
Character	Meaning
( )	        Grouping

Example:
r"cat|dog"

🔙 6. Escape Character
Character	Meaning
\	        Escape special characters

Example:
r"\."   # matches actual dot

🧠 7. Special Sequences (Very Important)
Character	Meaning
\b	        Word boundary
\B	        Not a word boundary
⚡ 8. Lookarounds (Advanced)
Character	Meaning
(?=...)	    Positive lookahead
(?!...)	    Negative lookahead
(?<=...)	Positive lookbehind
(?<!...)	Negative lookbehind
"""
import os
import re
os.system('cls')

# we can search this pattern from our text
pattern = "on"
text = ("""
         Machine learning is a field of artificial intelligence that focuses on building systems capable of learning from data
         rather than being explicitly programmed. Instead of writing fixed rules, developers train models on large datasets
         so they can identify patterns and make predictions. For example, a model trained on historical sales data can forecast future demand,
         while another trained on images can recognize objects or faces.) 
         There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.
         In supervised learning, models learn from labeled data, meaning the correct answers are already known. 
         Unsupervised learning deals with unlabeled data and focuses on discovering hidden structures or patterns.
         Reinforcement learning involves training an agent to make decisions by rewarding correct actions and penalizing mistakes.
         Data quality plays a critical role in the success of any machine learning system. Clean, well-structured data leads to 
         better model performance, while noisy or incomplete data can reduce accuracy. As machine learning continues to evolve,
         it is being applied in various industries such as healthcare, finance, and e-commerce, transforming how decisions are made
         and improving efficiency across systems.
""")
match = re.search(pattern, text)
# re.search stops by finding for first match
# pattern = "on" tell us whether 'on' is present in our text or not.
print(match)
# Output : <re.Match object; span=(78, 80), match='on'>
# re.Match object :  means a match is found
# span = (78, 80) : This shows the position of the match in the string
# 78 → starting index
# 80 → ending index (exclusive)
# match = on : This is the actual text that matched
# This output is basically saying:
#                                 “I found ‘on’ in your text, and it starts at index 78 and ends at 80.”
print(match.group())   # 'on'
print(match.start())   # 78
print(match.end())     # 80

# if we want an yclone starting with a capital letter, we can write pattern like :
pattern = r"[A-Z]+yclone"
# [] shows characters class
# 'r' shows raw string
text = ("""
        Natural Language Processing Cyclone (NLP) is a key area within machine learning that focuses on enabling computers to understand,
        interpret, and generate human language. It combines techniques from linguistics, computer science, and artificial intelligence
        to process text and speech data. NLP is widely used in applications such as chatbots, language translation, sentiment analysis,
        and voice assistants.
        In machine learning, NLP models are trained on large text datasets to learn patterns, context, and relationships between words.
        Traditional approaches included methods like bag-of-words and TF-IDF, while modern systems rely on deep learning models such as
        transformers. These models can cyclone capture context more effectively and generate more accurate results.
        One of the biggest challenges in NLP is dealing with ambiguity and context in language. Words can have multiple meanings depending
        on usage, making understanding difficult. Despite these challenges, NLP continues to evolve rapidly and plays a crucial role in improving
        human-computer interaction across industries Dyclone.
""")
# match = re.search(pattern, text)
matches = re.finditer(pattern, text)
for match in matches :
    # print(match)
    # print(match.span())
    # print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])

# Documentation of Regular Expressions : https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
# Python Docs for Regular Expressions : https://docs.python.org/3/library/re.html
# Complete Mastery of Regular Expressions : https://regexr.com/

"""
Exercise 1 — Email Extraction (Real World)
Task:
Extract all valid emails from the text.
text = """
" Contact us at support@gmail.com or sales123@yahoo.com."
" Invalid ones: test@com, user@.com, @gmail.com "
"""
Goal:
Output should be:
['support@gmail.com', 'sales123@yahoo.com']

Focus:
\w
+
@
\.
"""
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# [a-zA-Z0-9._%+-]+ → matches all valid characters in the username before @
# @[a-zA-Z0-9.-]+ → matches domain names, allowing dots and hyphens
# \.[a-zA-Z]{2,} → ensures a valid TLD, at least 2 letters (like .com, .org)
text = """
Contact us at support@gmail.com or sales123@yahoo.com.
Invalid ones: test@com, user@.com, @gmail.com
"""
matches = re.findall(pattern, text)
for match in matches :
    print(match)
"""
Exercise 2 — Words Ending with "ing"
Task:
- Extract all words that end with "ing"

text = "I am learning coding and building something amazing while testing regex parsing"
✅ Expected Output:
['learning', 'coding', 'building', 'something', 'amazing', 'testing', 'parsing']

Focus:
=> \b (word boundary)
=> pattern ending logic
"""
pattern = r"\b[a-zA-Z]+ing\b[.,!?:;]?"
text = """
       I am learning coding and building something amazing while testing regex parsing
"""
matches = re.finditer(pattern, text)
for match in matches :
    print(text[match.span()[0]:match.span()[1]])
"""
Exercise 3 — Clean the Text (Data Cleaning)
Task:
- Remove all punctuation from the text

text = "Hello!!! How are you??? I hope everything's fine :)"
Expected Output:
"Hello How are you I hope everythings fine "

Focus:
=> re.sub()
=> [^...] (negation)
"""
pattern = r"[^\w\s']"
'''
Explanation:
[] → defines a character class
^ → negates the class (matches anything not in it)
\w → matches word characters [a-zA-Z0-9_]
\s → matches whitespace (spaces, tabs, newlines)

So [^\w\s] → everything that is NOT a letter, number, or space (punctuation, symbols, etc.)
'''
text = """
       Hello!!! How are you??? I hope everything's fine :)
"""
matches = re.sub(pattern,"", text)
print(matches)

"""
Exercise 4 — Extract Proper Names (Capital Words Only)
Task:
=> Extract all proper names (words starting with capital letter)

text = "Ali went to Lahore and met Ahmed in Pakistan"
✅ Expected Output:
['Ali', 'Lahore', 'Ahmed', 'Pakistan']

Focus:
=> [A-Z]
=> [a-z]+
"""
# pattern = r"[A-Z][a-z]+"
pattern = r"[A-Z][a-z]+(?:['-][A-Z][a-z]+)?"
text = "Ali went to Lahore and met Ahmed in Pakistan"
matches = re.findall(pattern, text)
for match in matches :
    print(match)
"""
Bonus Challenge (This separates you)
Task:
=> Extract only valid Pakistani phone numbers

Valid:
03001234567
03111234567

Invalid:
3001234567
03001234

Logic:
=> Starts with 03
=> Total digits = 11
"""
pattern = r"03\d{9}"
text = """
      Valid:
      03001234567
      03111234567

      Invalid:
      3001234567
      03001234
"""
correct_numbers = re.finditer(pattern, text)
for match in correct_numbers :
    print(match)