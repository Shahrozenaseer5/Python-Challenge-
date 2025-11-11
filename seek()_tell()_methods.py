import os 
os.system('cls')

# f = open('seek()_tell().txt', 'r')
# lines = f.read()
# print(lines)
# f.close()
"""
seek(offset, whence) :
Purpose: Moves the cursor to a specific position.
Use : To jump to a different part of the file.

Parameters:
offset: Number of bytes to move.
whence: (optional) reference position. It can be:

0 → from the beginning of the file (default)
1 → from the current position
2 → from the end of the file
"""
f = open('seek()_tell().txt', 'r')
f.seek(6) # Move to the 6th byte from start
content = f.read()
print(content)
f.seek(8) # Move to the 8th byte from start
print(f.read())
f.seek(17) # Move to the 17th byte from start
print(f.read(10)) # Read next 10 characters from there

# Example using 'whence':
f = open('seek()_tell().txt', 'rb') # binary mode required for whence > 0
# f.seek(3, 0) # Move 5 bytes backward from the end
f.seek(-7, 2)
print(f.read()) # Read last 7 bytes
f.close()

"""
tell()
Purpose: It tells (returns) the current position of the file pointer.

The file pointer is an 'invisible cursor' that keeps track of where you are in the file.

=> Think of tell() like asking: “Where am I right now in the file?”
"""

f = open('seek()_tell().txt', 'r')
print(f.tell()) # Usually starts at 0 (beginning of file)
f.read(9)
print(f.tell()) # Now it will show 9, because 9 characters were read
f.read(23)
print(f.tell())
"""
=> tell() always measures bytes, not characters.
=> In text mode, decoding changes byte positions.
=> In binary mode, tell() shows the exact byte offset you expect.
"""
f.close()

f = open('seek()_tell().txt', 'rb') # In binary mode, tell() shows the exact byte offset you expect.
f.read(14)
print(f.tell())
f.close()
# tell() Returns: current position of file pointer (byte offset)

# Example : seek() + tell()
# Create a sample file
with open("sample.txt", "w") as f:
    f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # 26 characters

# Now open it for reading
with open("sample.txt", "rb") as f:
    print("Starting position:", f.tell())  # 0 (beginning)

    # Read first 5 characters
    data = f.read(5)
    print("After reading 5 chars:", f.tell())  # 5
    print("Data read:", data)

    # Move the pointer to position 10 (11th character)
    f.seek(10)
    print("After seek(10):", f.tell())  # 10

    # Read 3 characters from there
    data = f.read(3)
    print("Read 3 chars from pos 10:", data)
    print("Current position:", f.tell())

    # Move to 5 bytes before the end
    f.seek(-5, 2)
    print("Moved to 5 bytes before end:", f.tell())

    # Read the last 5 characters
    data = f.read()
    print("Last 5 characters:", data)
    print("Final position:", f.tell())

"""
Key takeaway :
Use "r" (text mode) → for reading characters.
Use "rb" (binary mode) → when working with exact byte positions or end-relative seeks.
"""
# truncate() function
"""
The truncate() function in Python is used with file objects to resize a file 
— meaning it cuts off (or extends) the file to a specific size in bytes.

Syntax :
file_object.truncate(size=None)

Parameters :

size (optional):
The number of bytes the file should keep.
If omitted, it truncates the file from the current file pointer position.

Returns :
Nothing (it just modifies the file)
"""
# Create a sample file
with open('truncate.txt', 'r+') as f : # r+ means reading and writing a file but file must be exist.
 f.write('Winter is coming, I am exited')

print("\nOriginal file content:")
with open('truncate.txt', 'r') as f :
   print(f.read())

# Example 1: Truncate to a specific size
with open('truncate.txt', 'r+') as f :
   f.truncate(12) # Keep first 12 characters

print("\nAfter truncating to 12 characters/bytes :")
with open('truncate.txt', 'r+') as f:
    content = f.read()
    print(content)
    print(f"(File is now {len(content)} characters long)")

# Example 2: Truncate from current pointer position
with open('truncate.txt', 'r+') as f:
   f.seek(6) # Move pointer to position 6
   f.truncate() # Remove everything after this position

print("\nAfter truncating from pointer at position 6:")
with open('truncate.txt', 'r') as f :
   print(f.read())

