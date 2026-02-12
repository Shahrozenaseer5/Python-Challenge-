"""
================================================================================
Project       : Daily Task Reminder with Logging and Voice Alerts
Author        : Shahroze
Created on    : 2026-02-13
Python Version: 3.x
Modules Used  : os, time, win32com.client
Purpose       : 
    - Demonstrates usage of Python's time module for delays, timestamps, 
      and performance measurement.
    - Implements automatic logging of events to a text file.
    - Provides real-time task reminders with SAPI voice notifications.
    - Shows performance comparison between different time measurement methods.

Features      :
    1. Automatic Logging System
       - Logs events with timestamps in 'log.txt'.
    2. Performance Timer
       - Measures elapsed time, CPU time, and high-resolution performance time.
    3. Daily Task Reminder
       - Reminds user of tasks at predefined hours using voice and console output.

Usage Notes   :
    - Ensure Windows OS with SAPI installed for voice notifications.
    - Adjust task schedule in the `schedule` dictionary as per requirement.
    - Logs are stored in the folder defined by `folder_path`.

================================================================================
"""

"""
Time module : 
             The time module lets Python pause, measure, and understand time using the system clock.

Purpose of the time module :
=> The time module is mainly used for:
=> Delays and waiting
=> Measuring execution time
=> Getting timestamps
=> Controlling flow based on time

1 - first way to sum all numbers (using a loop)
total = 0

for i in range(1, 1000001):
    total += i

print(total)

2 - we can use python shortcut
print(sum(range(1, 1000001)))
"""
import os 
os.system('cls')
import win32com.client as wincl
import time
# # time.time()
# start = time.time() # Return the current time in seconds since the Epoch.
# lst = [11,22,33,44,55,66,77,88,99]
# for i in lst :
#     print(i)
# end = time.time()
# print("Execution time:", end - start)

# # Example 2 : time.time()
# def usingWhile() :
#     i = 0
#     while i < 40000 :
#         i = i + 1 
#         print(i)

# def usingFor() :
#     for i in range(40000) :
#         print(i)

# init = time.time()
# usingFor()
# Runing_for_loop = time.time()-init

# init = time.time()
# usingWhile()
# Runing_while_loop = time.time()-init
# print(Runing_for_loop)
# print(Runing_while_loop)

# # time.sleep() => it will Pauses the program to that # of number of seconds we have given to it. 
# # e.g in time.sleep(2) program will wait for 2 seconds and then execute next part of code
# a = 32
# b = 31

# start = time.time()
# time.sleep(2)
# if a==b :
#     print('both are equal')
# elif a<=b :
#     print('a is less than b and both are equal')
# else : 
#     print('a is greater than b')
#     time.sleep(4)
# end = time.time()
# print("execution time : ", end-start)

# # time.ctime() Converts a timestamp into a human-readable string.
# dic = {'name' : 'Aliyaar', 'age' : 29, 'status' : 'Learning'}
# print(dic)
# print(time.ctime())

# # time.localtime() Returns a structured time object (year, month, day, etc.).
# # Useful when you need specific parts of the date or time.
# t = time.localtime()
# today = time.strftime("%A")
# print(t.tm_year)
# print(time.strftime("%A")) # %A means full weekday name
# print(t.tm_hour)
# print(t.tm_min)
# print(t.tm_sec)
# print(f"Today is {today}")
# # tm comes from “time structure”.
# # when we write : t.tm_hour, we are asking :  “Give me the hour part from the time structure”

# # time.strftime(format, time_object)
# # Formats time in a custom way
# now = time.localtime()
# formatted = time.strftime("%Y-%m-%d %H:%M:%S", now)
# print(formatted)

# # time.gmtime() Same as localtime() but in UTC
# """
# - time.gmtime() is a function in Python’s time module that gives you the current time in UTC (Coordinated Universal Time).
# - UTC is the “world standard time,” independent of your local time zone.
# - It returns a structured time object (called struct_time) that contains all the parts of the current UTC time.
# """
# utc_time = time.gmtime()
# print(utc_time)
# # This shows year, month, day, hour, minute, second, weekday, day-of-year, all in UTC, not local time.

# # time.perf_counter() High-resolution timer for benchmarking.
# start = time.perf_counter()
# # code to measure
# time.sleep(0.5)
# time.sleep(2.79)

# end = time.perf_counter()
# print(end - start)
# # Preferred over time.time() when measuring performance

# # time.process_time() Measures CPU time only, not sleep or waiting
# start = time.process_time()
# # CPU-bound work
# names = [
#     "Ahmed", "Aisha", "Omar", "Fatima",     # Middle East
#     "Arjun", "Priya", "Rahul", "Sana",      # South Asia
#     "Li Wei", "Chen", "Yuki", "Hiroshi",    # East Asia
#     "Maria", "Luca", "Sofia", "Andrei",     # Europe
#     "John", "Emily", "Michael", "Jessica",  # North America
#     "Carlos", "Diego", "Fernanda", "Amina", # Latin America & Africa
#     "Kwame", "Zainab", "Chinedu", "Noah",   # Africa
#     "Oliver", "Mia"                         # Europe / Global
# ]
# if 'PARESH' in names :
#    print('Yes')

# else : 
#     print('No')
# end = time.process_time()
# print(end - start)
# Useful in performance analysis

"""
Exercise 1: Automatic Logging System

Goal: Write a script that logs events with timestamps.

Task:
=> Create a program that simulates some events, e.g., ["Start process", "Load data", "Process data", "End process"].
For each event:
=> Print the event to console.
=> Record the exact timestamp using time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).
=> Add a pause of 1–2 seconds between events using time.sleep() to simulate processing.
=> Save the logs to a file named log.txt.

Observations :
- time.strftime()
- time.localtime()
- time.sleep()
- Basic file writing
"""
start = time.time()

folder_path = r"C:\Users\dell\Desktop\Python practice"
file_name = "log.txt"
file_path = os.path.join(folder_path, file_name)

def write_log(event_name):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(file_path, "a") as f:
        f.write(f"[{timestamp}] {event_name}\n")
    print(f"{event_name}")

# Simulated process
time.sleep(2)
write_log("Starting process")

time.sleep(2)
write_log("Loading data")

time.sleep(2)
write_log("Processing data")

time.sleep(2)
write_log("Program ended successfully")

end = time.time()
print("Program takes", end - start , "seconds to finish")

"""
Exercise 2: Performance Timer for a Loop

Goal: Measure real execution time vs CPU time.

Task:
=> Create a list of 1–1000000 numbers.
=> Sum all numbers using a loop.
=> Measure the time using:
=> time.time() → total elapsed time including sleep
=> time.perf_counter() → high-resolution measurement
=> time.process_time() → CPU-only time
=> Print all three times and compare.

Observations :
=> Difference between elapsed time and CPU time
=> time.time(), time.perf_counter(), time.process_time()
=> Timing loops for optimization
"""
start_1 = time.perf_counter()
cpu_start = time.process_time()
start_2 = time.time()
list_1 = [i for i in range(1000000)]
# print(list_1)
print(len(list_1))
print(list_1[-10:]) # it will print last 10 values of list "list_1"

time.sleep(2)

# Gauss formula (n(n+1)/2)
n = 1000000
total = n * (n+1) // 2 # we use // to get an integer instead of float
print(total)

time.sleep(2)
end_1 = time.perf_counter()
cpu_end = time.process_time()
end_2 = time.time()

print("Performance Counter : ", end_1 - start_1)
"""
- Total real-world time your program took.
- This includes the 2 + 2 seconds of sleep.
"""
print('CPU time : ', cpu_end - cpu_start)
"""
- This measures CPU time only
- It doesn't include sleep time (2+2=4 seconds) because during time.sleep(2) cpu does nothing
"""
print("Total elapsed time : ", end_2 - start_2)
"""
It works similar to perf_counter() for elapsed measurement, but:
- Lower resolution
- Can be affected if system clock changes
"""
"""
Exercise 3: Daily Reminder Program

Goal: Create a script that reminds the user of tasks at specific times.

Task:
=> Make a small list of tasks, e.g., ["Drink water", "Stretch", "Check emails"].
=> The script should run in a loop and:

=> Check the current hour using time.localtime() or time.gmtime().
=> Print a reminder if the current hour matches the predefined schedule (you can pick any hours for practice).
=> Add a time.sleep(60) at the end of the loop so it checks every minute.

Bonus: Format the time in a human-readable form with strftime() when printing the reminder.

Observations :
=> Real-time monitoring with time module
=> time.localtime() and time.gmtime()
=> strftime() formatting
=> Loops with pauses (sleep)
"""

# For checking only 1 time :

# Create the SAPI voice dispatcher object
# speaker = wincl.Dispatch("SAPI.SpVoice")
# # List of tasks
# tasks = ['Wake up', 'Exercise', 'Going to office', 'Lunch', 'Check mails', 'Come back home', 'Take bath', 'Sleeping']
# current_time=time.localtime()
# hour= current_time.tm_hour
# min= current_time.tm_min
# if hour == 8 and min == 35 :
#     print(tasks[1], time.strftime('%H : %M : %S', current_time))
# elif hour == 8 :
#     print(tasks[0] , time.strftime('%H : %M : %S', current_time))
# elif hour == 9 and min == 10 :
#     print(tasks[2], time.strftime('%H : %M : %S', current_time))
# elif hour == 12 and min == 30 :
#     print(tasks[3], time.strftime('%H : %M : %S', current_time))
# elif hour == 14 :
#     print(tasks[4], time.strftime('%H : %M : %S', current_time))
# elif hour == 17 and min == 30 :
#     print(tasks[5], time.strftime('%H : %M : %S', current_time))
# elif hour == 19 and min == 30 :
#     print(tasks[6], time.strftime('%H : %M : %S', current_time))
# else :
#     print(tasks[7] , time.strftime('%H : %M : %S', current_time))
#     speaker.Speak (tasks[7])
#     time.sleep(60)


# For checking reminders afters every second, we need loop :
speaker = wincl.Dispatch("SAPI.SpVoice")

tasks = ['Wake up', 'Exercise', 'Going to office', 'Lunch', 'Check mails', 'Come back home', 'Take bath', 'Sleeping']

# Optional: map tasks to specific times
schedule = {
    (8, 0): tasks[0],
    (8, 35): tasks[1],
    (9, 10): tasks[2],
    (12, 30): tasks[3],
    (14, 0): tasks[4],
    (17, 30): tasks[5],
    (19, 30): tasks[6]
}

while True:
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min

    task_to_do = schedule.get((hour, minute), tasks[7])  # default to "Sleeping"
    print(task_to_do, time.strftime('%H:%M:%S', current_time))
    speaker.Speak(task_to_do)

    time.sleep(60)  # wait 1 minute before checking again
