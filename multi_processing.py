"""
Project: Concurrency & Parallelism in Python (Hands-on Practice)
Author: Shahroze
Purpose:
    This project demonstrates practical understanding of:
    - Multithreading vs Multiprocessing
    - Task parallelism using ThreadPoolExecutor and ProcessPoolExecutor
    - I/O-bound vs CPU-bound workloads
    - Performance benchmarking using Python

Key Concepts Covered:
    - Concurrent execution using threads and processes
    - Worker pool tuning (max_workers)
    - Real-world file downloading simulation
    - Error handling in concurrent tasks
    - Execution time comparison (sequential vs parallel)

Note:
    This is a learning and experimentation project focused on Python concurrency
    and performance optimization techniques.

Libraries Used:
    - concurrent.futures
    - multiprocessing
    - threading
    - requests
    - time
    - os

Environment:
    Python 3.x
"""
"""
Multiprocessing is a way to run multiple processes at the same time, each with its own memory space and Python interpreter.
Instead of one CPU core doing tasks one by one, you use multiple cores in parallel.

Why we need multiprocessing ?
It’s useful when tasks are CPU-heavy, like:

- training ML models
- image processing
- large numerical computations

Because it actually speeds things up by using multiple CPU cores.

Multithreading vs Multiprocessing :

Multithreading :

- Multiple threads inside a single process
- Share the same memory
- Good for I/O tasks (file handling, web requests)
- Limited in Python due to GIL (Global Interpreter Lock), so CPU tasks don’t speed up much

Multiprocessing :

- Multiple separate processes
- Each has its own memory
- True parallel execution (uses multiple CPU cores)
- Best for CPU-intensive tasks

Simple difference :
Multithreading → “one brain, many hands”
Multiprocessing → “many brains working together”

When to use what :
=> Downloading files, APIs, web scraping → multithreading
=> Data processing, ML training, heavy calculations → multiprocessing

for images : https://picsum.photos/2000/3000
Shortcut for activity monitor on windows : Press Ctrl + Shift + Esc
"""
import multiprocessing
import concurrent.futures
import time
import threading
import concurrent.futures
import requests
import os

# create folder if it doesn't exist
# os.makedirs("files", exist_ok=True)

# def download_file(url, name):
#     response = requests.get(url)
#     with open(f"files/file_{name}.jpg", "wb") as f:
#         f.write(response.content)

# url = "https://picsum.photos/1800/2800"

# for i in range(1, 13):
#     download_file(url, i)

# with the help of multiprocessing, we will populate our files folder with 50 images :
# def download_file(url, name):
#     print(f"Start Downloading {name}")
#     response = requests.get(url)
#     with open(f"files/file_{name}.jpg", "wb") as f:
#         f.write(response.content)
#     print(f"Finish Downloading {name}")

# if __name__ == "__main__":
#     os.makedirs("files", exist_ok=True)
#     url = "https://picsum.photos/1800/2800"
#     pros = []
#     for i in range(1, 51):
#        # download_file(url, i)
#        p = multiprocessing.Process(target=download_file, args= [url, i])
#        p.start()
#        pros.append(p)

#     for p in pros:
#         p.join()

# Same thing with ProcessPoolExecuter
# url = "https://picsum.photos/1800/2800"
# if __name__ == "__main__":
#    with concurrent.futures.ProcessPoolExecutor() as executor:
#        l1 = [url for i in range(60)]
#        l2 = [i for i in range(60)]
#        results = executor.map(download_file, l1, l2)
#        for r in results:
#            print(r)

"""
Exercise 1: Compare Speed 

Run your downloader in three ways:

Normal loop
Multithreading (ThreadPoolExecutor)
Multiprocessing (ProcessPoolExecutor)

Measure time using time.time() and compare.

👉 Goal: See when multiprocessing helps and when it doesn’t (hint: downloading is I/O, not CPU).
"""
def download_file(url, name, folder):
    response = requests.get(url)
    with open(f"{folder}/file_{name}.jpg", "wb") as f:
        f.write(response.content)
    return f"Image-{name} downloaded"

if __name__ == "__main__":
   url = "https://picsum.photos/1800/2800"
   start = time.perf_counter()
   for i in range(1, 51):
       download_file(url, i, "files")
   end = time.perf_counter()
   print(f"Sequencial coding: {end - start} seconds")

# with ThreadPoolExecutor
   start = time.perf_counter()
   def pooling():
           with concurrent.futures.ThreadPoolExecutor() as executor:
               lst_1 = [i for i in range(1, 51)]
               lst_2 = [url for _ in range(1, 51)]
               results = executor.map(download_file, lst_2, lst_1, ["thread files"]*50)
               for r in results :
                  print(r)
   pooling()
   end = time.perf_counter()
   print(f"threading: {end - start} seconds")

   # with ProcessPoolExecutor
   url = "https://picsum.photos/1800/2800"
   start = time.perf_counter()
   with concurrent.futures.ProcessPoolExecutor() as executor:
       lst_1 = [url for i in range(1, 51)]
       lst_2 = [i for i in range(1, 51)]
       results = executor.map(download_file, lst_1, lst_2, ["processes files"]*50)
       for r in results :
           print(r)

   end = time.perf_counter()
   print('multiprocessing',end - start)
"""
Exercise 2: Control Number of Workers

Modify your ProcessPool code:
=> with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
Try with:
2 workers
4 workers
8 workers
👉 Goal: Understand too many processes can slow things down.
"""
def download_file(url, name, folder):
    response = requests.get(url)
    with open(f"{folder}/file_{name}.jpg", "wb") as f:
        f.write(response.content)
    return f"Image-{name} downloaded"

if __name__ == "__main__":
   # with ProcessPoolExecutor
   url = "https://picsum.photos/1800/2800"
   start = time.perf_counter()
   # with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
   # with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
   with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
       lst_1 = [url for i in range(1, 51)]
       lst_2 = [i for i in range(1, 51)]
       results = executor.map(download_file, lst_1, lst_2, ["processes files"]*50)
       for r in results :
           print(r)

   end = time.perf_counter()
   print('multiprocessing',end - start)
   # Conclusion :
   # if max_workers = 2 , total time will be 70 sec
   # if max_workers = 4 , total time will be 41 sec
   # if max_workers = 8 , total time will be 28 sec
# As max_workers increases, performance improves initially because more tasks run in parallel. 
# However, after a certain point, gains reduce due to network and system limitations.
"""
Exercise 3: Return Results Properly
Update your function:

def download_file(url, name):
    response = requests.get(url)
    with open(f"files/file_{name}.jpg", "wb") as f:
        f.write(response.content)
    return f"Downloaded file {name}"

Now print meaningful results.
👉 Goal: Learn how data flows back from processes.
"""
def download_file(url, name):
    response = requests.get(url)
    with open(f"thread files/file_{name}.jpg", "wb") as f:
        f.write(response.content)
    return f"Downloaded file {name}"

if __name__ == "__main__":
    start = time.perf_counter()
    url = "https://picsum.photos/1800/2800"
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        lst_1 = [url for i in range(1, 51)]
        lst_2 = [i for i in range(1, 51)]
        results = executor.map(download_file, lst_1, lst_2)
        for r in results:
            print(r)

    end = time.perf_counter()
    print('threading : ', end - start, 'seconds')

"""
Exercise 4: Add Error Handling (Real-world skill)
Modify your function:

def download_file(url, name):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        with open(f"files/file_{name}.jpg", "wb") as f:
            f.write(response.content)
        return f"Success {name}"
    except Exception as e:
        return f"Failed {name}: {e}"

👉 Goal: Handle failures gracefully, like real systems.
"""

def download_file(url, name):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        with open(f"files/file_{name}.jpg", "wb") as f:
            f.write(response.content)
        return f"Success {name}"
    except Exception as e:
        return f"Failed {name}: {e}"

if __name__ == "__main__":
    url = "https://picsum.photos/1800/2800"
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        l1 = [url for i in range(1,41)]
        l2 = [i for i in range(1,41)]
        results = executor.map(download_file, l1, l2)
        for r in results:
            print(r)

    end = time.time()
    print('threading : ',end - start, 'sec')