"""
================================================================================
Project Name: Shoutout Speaker
File Name   : Ex9_ShoutoutToEveryone.py
Author      : Shahroze
Date        : 2026-02-05
Description : This script uses Windows SAPI via pywin32 to pronounce a list of 
              names. For each name in the provided list, it outputs a console 
              message and speaks "Shoutout to <Name>" using the system's 
              text-to-speech engine. Supports voice selection and basic 
              configuration (rate, volume).

Requirements:
    - Python 3.x (Windows)
    - pywin32 library

Usage:
    1. Ensure Python and pywin32 are installed on a Windows system.
    2. Modify the `names` list with the names you want to pronounce.
    3. Run the script in a terminal or VS Code. The program will print each 
       name and speak it aloud.

Notes:
    - Female and male voices can be selected by changing the index in 
      `speaker.Voice = voices.Item(index)`.
    - Time delays can be added for natural pacing using `time.sleep()`.
================================================================================
"""

"""
Write a program to pronounce list of names using win32 API. 
If you are given a list l as follow :
l = ['Rahul', 'Ahmad', 'John', 'Amna']
Your program should pronounce : 
Shoutout to Rahul
Shoutout to Ahmad
Shoutout to John
Shoutout to Amna
"""
import os 
os.system('cls')
# import win32api
import win32com.client as wincl
names = [
         "Ahmed", "Aisha", "Omar", "Fatima", "Arjun", "Priya", "Rahul", "Sana", "Li Wei", "Chen", "Yuki",
         "Hiroshi", "Maria", "Luca", "Sofia", "Andrei", "John", "Emily", "Michael", "Jessica", "Carlos",
         "Diego", "Fernanda", "Amina", "Kwame", "Zainab", "Chinedu", "Noah", "Oliver"
        ]
# print(win32api.GetComputerName())

# Dispatch connects Python to a Windows component that already exists in the system
# Create the SAPI voice dispatcher object
speaker = wincl.Dispatch("SAPI.SpVoice")

# List all voices
for i, voice in enumerate(speaker.GetVoices()):
    print(f"{i}: {voice.GetDescription()}")

# Select a female voice
voices = speaker.GetVoices()
speaker.Voice = voices.Item(1)  # choose the correct index after checking

for name in names :
   # Text you want the computer to speak
   text = f'Shoutout to {name}'
   print(text) # print to console

  # Use the Speak method to speak the text
   speaker.Speak(text)