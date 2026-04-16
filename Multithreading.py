"""
===============================================================================
Topic: Multithreading in Python
Author: Shahroze
Purpose: Learning, practicing, and demonstrating multithreading concepts
Module(s): threading, concurrent.futures, time
===============================================================================

Overview:
This file covers the fundamentals of multithreading in Python, including:
- Conceptual understanding (what, why, when)
- Limitations (GIL and CPU-bound constraints)
- Practical usage with threading and ThreadPoolExecutor
- Comparison of sequential vs concurrent execution
- Real-world simulation (API calls)
- Hands-on exercises with timing analysis

-------------------------------------------------------------------------------

Key Concepts:

✔ Multithreading:
Running multiple lightweight tasks (threads) within the same process
to improve efficiency, especially for I/O-bound operations.

✔ Concurrency:
Managing multiple tasks by switching between them efficiently.

✔ GIL (Global Interpreter Lock):
Allows only one thread to execute Python bytecode at a time.
→ Threads are NOT effective for CPU-heavy tasks.

✔ Heuristic:
A rule-of-thumb approach Python uses to choose default thread count.

-------------------------------------------------------------------------------

When to Use Multithreading:

✅ I/O-bound tasks:
- API calls
- File handling
- Web scraping
- Database operations

❌ Avoid for CPU-bound tasks:
- Heavy calculations
- Machine Learning training
- Image processing

→ Use multiprocessing instead for CPU-heavy work.

-------------------------------------------------------------------------------

Tools Covered:

1. threading module
   - Manual thread creation
   - start() and join()

2. concurrent.futures
   - ThreadPoolExecutor
   - submit()
   - map()
   - as_completed()

-------------------------------------------------------------------------------

Execution Behavior:

- Threads run concurrently (not strictly parallel)
- Execution order may vary
- Result order depends on method used:

    map()              → preserves input order
    submit() + loop    → manual control
    as_completed()     → completion order

-------------------------------------------------------------------------------

Exercises Included:

1. Sequential vs Threaded execution
2. Understanding concurrency vs result order
3. Simulating real-world API calls with timing comparison

-------------------------------------------------------------------------------

Key Insight:

Multithreading does NOT make tasks faster.
It reduces idle time by handling multiple waiting tasks simultaneously.

Rule:
WAITING (I/O) → Use threads
WORKING (CPU) → Avoid threads

-------------------------------------------------------------------------------

🔗 Reference:
https://docs.python.org/3/library/concurrent.futures.html

===============================================================================
"""

"""
Multithreading :
                Multithreading means running multiple threads (lightweight tasks) within the same process at the same time.
- Think of a thread as a worker.
One program → multiple workers → doing tasks together

Example idea:

- One thread downloads a file
- Another updates UI
- Another logs data

- All inside the same program.

Simple Analogy

Imagine you’re running a shop:
=> You (single thread):
→ Take order → pack → bill → deliver (one by one)
=> With helpers (multithreading):
→ One takes orders
→ One packs
→ One handles billing

Work becomes faster if tasks can overlap.

Why Do We Need Multithreading?
- Because many real-world programs are waiting most of the time, not computing.

Examples of waiting:
- Network requests
- File reading/writing
- API calls
- Database queries

Instead of wasting time waiting, threads allow:
👉 “Do something else while waiting”

Important Reality (Very Important for Interviews)
Python has something called:
👉 Global Interpreter Lock (GIL)
Meaning:
- Only one thread executes Python bytecode at a time.
- So threads don’t speed up CPU-heavy tasks.
Means If your program is doing heavy thinking (calculations), adding more threads will NOT make it faster in Python.

When Should You Use Multithreading?
✅ Good for (I/O-bound tasks):
- File downloads
- API calls
- Web scraping
- Database operations
❌ Bad for (CPU-bound tasks):
- Heavy calculations
- Machine Learning training
- Image processing
For CPU tasks → use multiprocessing, not multithreading

Benefits of Multithreading :
- Better responsiveness (UI doesn’t freeze)
- Faster execution for I/O tasks
- Efficient use of waiting time
- Lightweight compared to processes

for using multithreading, we write :
                                    import threading
Basic Syntax :
import threading

def task():
    print("Task running")

t1 = threading.Thread(target=task)

t1.start()   # start thread
t1.join()    # wait for thread to finish

print("Done")

Multithreading Example :
import threading
import time

def task(name):
    for i in range(3):
        print(f"{name} running")
        time.sleep(1)

t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()
=> Both threads run “together” (interleaved execution)

Real-Life Use Cases :
1. File Downloader
- Download multiple files at once instead of one by one

2. Web Scraper
- Scrape multiple websites simultaneously

3. API Aggregator
- Fetch data from multiple APIs at the same time

4. Background Tasks
- Logging
- Notifications
- Auto-saving
5. GUI Applications
- Prevent UI freezing (buttons still clickable while work runs)

Multithreading vs Asyncio (Important Difference) :

Feature                	Multithreading	                Asyncio
Style	                 Threads	                     Single thread + event loop
Best for	             I/O tasks	                     High-scale I/O tasks
Complexity	             Medium	                         Higher (conceptually)
Control	                 Less control	                 More control

👉 In modern Python:
- Asyncio is often preferred for scalable apps
- Threads are simpler for smaller tasks

When You Should NOT Use Multithreading
1. CPU-Heavy Work (Biggest One)-
If your task is pure computation, avoid threads.

Examples:

- Machine learning training
- Image processing
- Large mathematical calculations
- Data transformations on huge datasets

Why?

👉 Because of Global Interpreter Lock (GIL)
Only one thread uses the CPU at a time → no real speed gain

👉 Sometimes it even becomes slower due to switching overhead

2. When Tasks Depend on Each Other
If tasks must happen in strict order:
Example:
Step 1 → Step 2 → Step 3 (dependent pipeline)

Threads can:
- Break order
- Create inconsistent results
👉 In such cases, simple sequential code is safer

3. When You’re Modifying Shared Data
Example:
balance = 1000

Two threads:
- Both read balance = 1000
- Both update it

👉 Result becomes wrong (race condition)

Problems:
- Data corruption
- Random bugs (very hard to debug)
4. When the Task Is Already Fast
If your task takes:
- milliseconds

Then threading adds:
- overhead
- complexity
👉 Result: slower + messy code

5. When You Need Maximum Performance (CPU Work)
If performance is critical:
👉 Use:
- multiprocessing
- or optimized libraries (NumPy, etc.)
=> Threads won’t help here

6. When Debugging Matters More Than Speed
Threads introduce:
- unpredictable behavior
- timing issues
👉 Bugs become:
- hard to reproduce
- hard to fix

=> For beginners → this becomes frustrating fast

7. When Asyncio Is a Better Fit
If you are handling:
- thousands of network requests
- scalable APIs
- real-time systems

👉 Asyncio is usually better than threads

=>Threads don’t scale well in large numbers

🔹 Simple Rule You Can Remember
Before using threads, ask:
👉 “Is my program WAITING or WORKING?”

WAITING (I/O) → ✅ use threads
WORKING (CPU) → ❌ don’t use threads
🔹 Real-Life Comparison
❌ Don’t use threads:
Training ML model
Processing 1M rows of data
Running heavy calculations
✅ Use threads:
Downloading 20 files
Calling multiple APIs
Reading multiple files
🔹 One Honest Insight :
Most beginners misuse multithreading because:

- It sounds like “more threads = more speed”
But in Python, that’s not true.

Important Note :
- Every server has its own speed unless the speed of our internet
- So it's better to hit 5-10 or more servers parallely (at the same time) according to our need

concurrent.futures :
- it's a built-in module in python. "ThreadPoolExecutor" is another tool in concurrent.futures.
- We can submit function to it and get desired results.
- for parallel execution, concurrent.futures is very helpful
Syntax :
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

- In ThreadPoolExecutor, we control concurrency using max_workers (number of threads allowed to run tasks).
- Concurrency -> managing multiple tasks at once by switching between them efficiently
max_workers=1 → runs tasks sequentially (no real multithreading effect)
max_workers > 1 → enables real concurrent execution using multiple threads
max_workers not specified → Python chooses a default value based on system resources (usually number of CPU cores or a heuristic)

Heuristic simply means:
                      a rule of thumb or a smart shortcut used to make a good enough decision quickly, without doing full calculations.

=> If we want to download 50 or more urls, concurrent.futures module makes it easy for us.

=> Threads run in parallel, but map() always returns results in the same order you gave input

Method	                         Output order
map()	                          same as input order
submit() + loop	                  manual control
as_completed()	                  completion order

=> as_completed() returns results as soon as each thread finishes, not in input order
Documentation of concurrent.futures :
https://docs.python.org/3/library/concurrent.futures.html
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# indicates some task being done
# def func(seconds) :
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)
#     return seconds

# Normal code
# time1 = time.perf_counter()
# func(4) # takes 4 seconds to run
# func(3) # takes 3 seconds to run
# func(2) # takes 2 seconds to run
# time2 = time.perf_counter()
# print('time taken without threads : ',time2 - time1, 'seconds')

# same code using threads
# time1 = time.perf_counter()
# t1 = threading.Thread(target = func, args = [4])
# t2 = threading.Thread(target = func, args = [3])
# t3 = threading.Thread(target = func, args = [2])
# to start functionality, we write :
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# time2 = time.perf_counter()
# calculating time
# print('time taken with threads : ',time2 - time1, 'seconds')
# Always remember : "slowest step is the rate limiting step"

# def main():
#     time1 = time.perf_counter()
#     t1 = threading.Thread(target = func, args = [4])
#     t2 = threading.Thread(target = func, args = [3])
#     t3 = threading.Thread(target = func, args = [2])
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     time2 = time.perf_counter()
#     print('time taken with threads : ',time2 - time1, 'seconds')
#
# def poolingDemo():
#
#     with ThreadPoolExecutor(max_workers > 1) as executor:
        # future1 = executor.submit(func, 4) # we submit function name and argument to executor
        # future2 = executor.submit(func, 3)
        # future3 = executor.submit(func, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

# syntax 2 : ThreadPoolExecutor with map (for larger lists)
#         l = [3, 5, 9, 2]
#         results = executor.map(func, l)
#         for result in results :
#           print(result)
# poolingDemo()
"""
Exercise 1 (Basic)
Goal: See difference between sequential vs threading
- Write two versions of this:

def task(n):
    print(f"Task {n} started")
    time.sleep(n)
    print(f"Task {n} finished")
Requirements:
- Run task(3), task(2), task(1) normally (no threads)
- Then run same using ThreadPoolExecutor
What you should observe:
- total time difference
- order difference in output
"""
def task(n):
    print(f"Task {n} started")
    time.sleep(n)
    print(f"Task {n} finished")
    return n

# Normal code
task(3)
task(2)
task(1)

# with threads
def poolingDemo():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, [3, 2, 1])
    print(list(results))

poolingDemo()

"""
Exercise 2 (Real Thread Behavior)
Goal: Understand concurrency vs order

=> Create a list:
l = [2, 4, 1, 3]
Task:
Use ThreadPoolExecutor to:
- print “Start X”
- sleep X seconds
- return X
Then print all results using:
print(list(results))
Challenge:
👉 Try with max_workers=2 and max_workers=4
- Observe difference in execution behavior
"""
def task2(x) :
    print(f"Task {x} started")
    time.sleep(x)
    return x

def pooling():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(task2, x) for x in [3, 5, 7]]

    for f in as_completed(futures):
        print(f.result())
# def pooling():
#     # with ThreadPoolExecutor() as executor:
#     # with ThreadPoolExecutor(max_workers = 2) as executor:
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         results = executor.map(task2, [3, 5, 7])
#     print(list(results))

pooling()

"""
Exercise 3 (Real-world simulation)
Goal: Simulate API calls

Imagine this function:

def fetch_data(api_name, delay):
    print(f"Calling {api_name}")
    time.sleep(delay)
    return f"{api_name} response"
Task:
Run these APIs:

apis = [
    ("google", 3),
    ("github", 2),
    ("openai", 4),
    ("stackoverflow", 1)
]
Requirements:
- Run sequentially first
- Then run using ThreadPoolExecutor
- Print total time for both
"""
# normal code
def fetch_data(api_name, delay):
    print(f"Calling {api_name}")
    time.sleep(delay)
    return f"{api_name} response"
time_1 = time.perf_counter()
fetch_data("google", 3)
fetch_data("github", 2)
fetch_data("openai", 4)
fetch_data("stackoverflow", 1)
time_2 = time.perf_counter()
print('Time taken normally : ', time_2 - time_1)

# using ThreadPoolExecutor
def fetch_data1(api_name, delay): # fetch_data1 is threaded worker
    print(f"Calling {api_name}")
    time.sleep(delay)
    return f"{api_name} response"
def fetch_data2(): # fetch_data2 is thread manager
    time_1 = time.perf_counter()
    apis = [
        ("google", 3),
        ("github", 2),
        ("openai", 4),
        ("stackoverflow", 1)
    ]
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(lambda p: fetch_data1(*p), apis)
    print(list(results))

    time_2 = time.perf_counter()
    print('Time taken  : ', time_2 - time_1)
fetch_data2()