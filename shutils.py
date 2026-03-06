"""
--------------------------------------------------------------------------------
Project       : Python File & Folder Management Practice
File          : shutils.py
Author        : Shahroze
Date          : 2026-03-07
Python Version: 3.12
Environment   : Google Colab (tested)

Description:
This script demonstrates advanced file and folder management using Python's 
built-in 'shutil' and 'os' modules. It covers:
    - Copying files and folders (with metadata preservation)
    - Moving files and folders
    - Deleting files and folders safely
    - Creating ZIP archives from multiple folders
    - Checking and handling existing files/folders to avoid errors

Intended Use:
- Learning and practicing high-level file operations
- Creating backup archives of multiple directories
- Safe folder manipulation in Google Colab environment

Usage Notes:
- Ensure that source folders/files exist before copying or moving.
- Be cautious with shutil.rmtree(): it permanently deletes files/folders.
- The script handles existing folders/files gracefully using checks and 
  'dirs_exist_ok=True' for copytree operations.

--------------------------------------------------------------------------------
"""
"""
Shutils module :
                shutil stands for shell utilities. It is a built-in Python module that provides high-level file and directory operations.
                shutil gives you ready-made tools for common file management tasks like:
                => Copying files
                => Copying entire folders
                => Moving files
                => Deleting directories
                => Creating archives (zip, tar, etc.)

How does shutil work?
=> It works on top of the os module.
=> Internally, many shutil functions use os functions. But instead of you manually writing logic
to copy file content or move files, shutil gives you one clean function to do it.

Example:

import shutil
shutil.copy("source.txt", "destination.txt")

Why do we need shutil?

Because writing file-handling logic manually is:
=> Time-consuming
=> Error-prone
=> More code to maintain

Imagine copying a full directory with subfolders using only os. You would need loops, checks, file reading, writing, path handling, etc.

With shutil, it’s just:

shutil.copytree("source_folder", "destination_folder")
Much cleaner.
So we use shutil when we want efficient file management with minimal code.

Key Difference: os vs shutil
Think of it like this:

os module → Low-level control
shutil module → High-level file operations

Clear comparison:

os Module	                                   shutil Module
Works with OS-level features	      Works mainly with files & directories
Create/delete files & folders	      Copy/move/delete files & folders
Handles environment variables	      Creates archives (zip, tar)
Provides path utilities	              High-level file manipulation

Example difference :

Create folder:

import os
os.mkdir("new_folder")

Copy folder:

import shutil
shutil.copytree("folder1", "folder2")

Notice:
=> os doesn’t directly copy directories.
=> shutil is built specifically for that.

What functionalities can shutil perform?

Here are the most important ones:

1. Copy files
shutil.copy("file1.txt", "file2.txt")

2. Copy file with metadata
shutil.copy2("file1.txt", "file2.txt")
(preserves timestamps etc.)

3. Copy entire directory / folder
shutil.copytree("source", "destination")

4. Move files or folders
shutil.move("file.txt", "new_location/file.txt")

5. Delete entire directory
shutil.rmtree("folder_name")

Very powerful. Be careful. It permanently deletes.

6. Create archives (ZIP, TAR)
shutil.make_archive("backup", "zip", "folder_to_backup")

7. Disk usage info
shutil.disk_usage("/")

When should we use which?

Use os when:
=> You need system-level control
=> Working with paths
=> Managing environment variables
=> Getting current directory

Use shutil when:
=> You need to copy/move/delete files or folders
=> You want quick file management
=> You need to create backups or archives

"""
import shutil
import os 
import time 
# shutil.copy() is used for file operations
# shutil.copy('shutils.py', 'shutil2.py')

# shutil.copy2() is used for copy file and meta data 
# shutil.copy2('shutils.py', 'shutil2.py')

# reading file data
# with open("shutil2.py", "r") as f:
#     print(f.read())
# We will see meta-data of copied file by using os module and time module
# info = os.stat("shutil2.py") 
# os.stat() returns a 'stat object' containing file metadata.
# print("Last Access:", time.ctime(info.st_atime))
# print("Last Modified:", time.ctime(info.st_mtime))

# -----------------------------------
# (for google colab only)
# from google.colab import files
# files.upload()
# ------------------------------------

# we use shutil.copytree() to copy an entire folder
# shutil.copytree('/var','my_nowels')
# shutil.copytree('/content/sample_data', '/content/ML-data', dirs_exist_ok=True)
# Source: /content/sample_data → the folder you want to copy
# Destination: /content/ML-data → the new folder that will be created as a copy

# shutil.move() is used to move a file to a specific location
# shutil.move('/content/shutil2.py', 'shutil2.py')
# shutil.move('/content/ML-data', '/content/sample_data/ML-data')
# shutil.move('/content/sample_data/ML-data/web', '/datalab')

# Delete folder if it exists
if os.path.exists('ML-data'):
    shutil.rmtree('ML-data')

if os.path.exists('my_nowels'):
    shutil.rmtree('my_nowels')

# Delete a file if it exists
if os.path.exists('shutil2.py'):
    os.remove('shutil2.py')

if os.path.exists('shutils.py'):
  os.remove('shutils.py')

shutil.copytree('/content/sample_data', '/content/ML-data' , dirs_exist_ok=True)
shutil.copytree('/content/sample_data', '/content/data-analytics' , dirs_exist_ok=True)
shutil.copytree('/content/sample_data', '/content/data-processing' , dirs_exist_ok=True)

# Step 1: Create a parent folder
os.makedirs('/content/all_folders', exist_ok=True)

# Step 2: Move or copy the folders inside the parent folder
shutil.copytree('ML-data', 'all_folders/ML-data' , dirs_exist_ok=True)
shutil.copytree('data-processing', 'all_folders/data-processing' , dirs_exist_ok=True)
shutil.copytree('data-analytics', 'all_folders/data-analytics' , dirs_exist_ok=True)

# Step 3: Make a ZIP archive of the parent folder
shutil.make_archive('combined_folders', 'zip', 'all_folders')

# Verify
print("ZIP created:", os.listdir())