"""
================================================================================
Exercise 11 : Drink Water Reminder
================================================================================
Author      : Shahroze
Date        : 29-Mar-2026
Language    : Python 3.x
Dependencies: pyttsx3, plyer
OS          : Cross-platform (Windows/Linux/macOS)

Description :
This Python program reminds the user to drink water every 2 hours.
It sends a desktop notification and uses text-to-speech to announce
the reminder. The program keeps track of reminders to prevent repeats
within the same hour.

Problem Statement :
- Write a Python program which reminds you of drinking water every hour or two.
- Your program can either beep or send desktop notifications for a specific OS.

Usage :
- Ensure dependencies are installed: `pip install pyttsx3 plyer`
- Run the script in a terminal or IDE.
- Keep it running in the background to receive reminders.

================================================================================
"""

import os
import time
import pyttsx3
import plyer
from plyer import notification

os.system('cls')
now = time.localtime()
print(now.tm_hour)
print(now.tm_min)
print(now.tm_sec)
engine = pyttsx3.init()     # initialize TTS engine
last_hour = -1   # define once before the loop
while True :
    now = time.localtime()
    a = now.tm_hour
    b = now.tm_min
    if a % 2 == 0 and b == 0 :
        if last_hour != a :
           print("Reminder triggered!")
           # trigger notification + voice
           last_hour = a  # remember that we triggered this hour
           notification.notify(
               title="Reminder",
               message="Drink water!",
               timeout=5
        )
           engine.say("Drink water! Time to stay hydrated.")     # tell engine what to say
           engine.runAndWait()        # play the speech
    time.sleep(30)