"""
Project: Async vs Sync API Data Fetcher
Author: Shahroze
Date: 2026
Description:
    This project demonstrates the difference between synchronous and asynchronous
    I/O operations in Python using real API requests.

    The asynchronous version uses asyncio and aiohttp to perform concurrent
    API calls, while the synchronous version uses requests to execute calls
    sequentially.

Features:
    - Concurrent API fetching using asyncio
    - Connection handling using aiohttp.ClientSession
    - Concurrency control using asyncio.Semaphore
    - Error handling for failed requests
    - Performance comparison (Async vs Sync)

Technologies Used:
    - Python
    - asyncio
    - aiohttp
    - requests
    - time

Learning Objectives:
    - Understand blocking vs non-blocking I/O
    - Implement async/await patterns
    - Manage multiple tasks using asyncio.gather
    - Control concurrency using semaphores
    - Compare performance between sync and async approaches
"""

"""
AsyncIO : 
         AsyncIO is a programming pattern that allows high-performance I/O operations in a
         non-blocking way, meaning the program can handle multiple tasks at the same time
         without waiting for each one to finish.

Synchronous vs Asynchronous I/O :
1. Synchronous I/O (Blocking)

=> In synchronous I/O, your program waits for a task to finish before moving on.

Behavior:
- One task at a time
- If something is slow → everything pauses
Example:
import time

def fetch_data():
    print("Fetching...")
    time.sleep(2)   # simulating delay
    print("Done")

fetch_data()
fetch_data()
What happens:
- First call waits 2 sec
- Second call starts after that
- Total ≈ 4 seconds

👉 This is called blocking

2. Asynchronous I/O (Non-blocking)

=> In async I/O, your program does not wait. While one task is waiting, it switches to another.

Behavior:
- Multiple tasks can progress together
- Waiting time is utilized
Example:
import asyncio

async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(2)
    print("Done")

async def main():
    await asyncio.gather(fetch_data(), fetch_data())

asyncio.run(main())
What happens:
- Both tasks start together
- Total ≈ 2 seconds

👉 This is non-blocking

Key Differences :
Feature	                 Synchronous I/O	                 Asynchronous I/O
Execution	              One by one	                      Overlapping tasks
Waiting	                  Blocks program	                  Doesn’t block
Speed (I/O tasks)	      Slower	                          Faster
Complexity	              Simple	                          Slightly complex
Tools	                  time.sleep()	                      asyncio, await
Real-Life Analogy :
Synchronous :
- Cook rice → wait
- Then cook curry → wait
- Then make salad
Asynchronous :
- Start rice
- While it cooks → make salad
- While that → prepare curry

👉 Same time, more efficiency

When to use each?
✅ Use Synchronous when:
- Tasks are simple
- No heavy waiting involved
- Scripts, small programs
✅ Use Asynchronous when:
- Network calls (APIs, scraping)
- Multiple requests at once
- Bots, servers, real-time apps

One-line clarity :
Synchronous → “Do this, then next”
Asynchronous → “Start this, while waiting do something else”
"""
import time
import requests
import aiohttp
import asyncio
# start = time.perf_counter()
# def function_1() :
#     time.sleep(3)
#     print('func_1')
# def function_2() :
#     time.sleep(3)
#     print('func_2')
# def function_3() :
#     time.sleep(3)
#     print('func_3')
#
# function_1()
# function_2()
# function_3()
# end = time.perf_counter()
# print('Time taken for synchronous IO :', end - start, 'seconds')
#
# start = time.perf_counter()
#
# async def async_function_1():
#     await asyncio.sleep(3)  # simulating I/O delay (like API call)
#     print('func_1')
#
# async def async_function_2():
#     await asyncio.sleep(3)
#     print('func_2')
#
# async def async_function_3():
#     await asyncio.sleep(3)
#     print('func_3')
#
# async def main_1():
#     await asyncio.gather(
#         # task=asyncio.create_task(function_1())
#         async_function_1(),
#         async_function_2(),
#         async_function_3()
#     )
# asyncio.run(main_1())
# end = time.perf_counter()
# print('Time taken for asynchronous IO:', end - start, 'seconds')
#
# async def photo_1():
#     print('pic_1')
#     url = "https://as2.ftcdn.net/jpg/05/75/56/99/1000_F_575569969_GpnPXACpktBN2OH8kcFzAvbIdJ9hRIJI.jpg"
#     response = requests.get(url)
#
#     # Always check if the request was successful
#     if response.status_code == 200:
#         with open('local_image.png', 'wb') as f:
#             f.write(response.content)
#
# async def photo_2():
#     print('pic_2')
#     url = "https://static.vecteezy.com/system/resources/thumbnails/049/855/272/small/nature-background-high-resolution-wallpaper-for-a-serene-and-stunning-view-photo.jpg"
#     response = requests.get(url)
#
#     # Always check if the request was successful
#     if response.status_code == 200:
#         with open('local_image.png', 'wb') as f:
#             f.write(response.content)
#
# async def photo_3():
#     url = "https://c4.wallpaperflare.com/wallpaper/813/588/839/special-effects-city-lights-artwork-electricity-wallpaper-preview.jpg"
#     response = requests.get(url)
#
#     # Always check if the request was successful
#     if response.status_code == 200:
#         with open('local_image.png', 'wb') as f:
#             f.write(response.content)
#     print('pic_3')
#
# async def main_2():
#         await asyncio.gather(
#             photo_1(),
#             photo_2(),
#             photo_3()
#         )
# asyncio.run(main_2())

"""
Exercise 1 — Basic async timing (foundation)
Goal:
- To Understand how tasks run “at the same time”

Task:
- Create 3 async functions:

Each should:
print “Start X”
wait (asyncio.sleep) for different times (e.g., 1s, 2s, 3s)
print “End X”

Then run them using asyncio.gather()

✅ Expected learning:
Order of execution will feel “mixed”
Total time ≈ longest task, not sum
"""
start = time.perf_counter()
async def task_1():
    print('Start function 1')
    await asyncio.sleep(1)
    print('End of function 1')

async def task_2():
    print('Start function 2')
    await asyncio.sleep(2)
    print('End of function 2')
async def task_3():
    print('Start function 3')
    await asyncio.sleep(3)
    print('End of function 3')

async def main_3():
    print('All tasks started')
    await asyncio.gather(
        task_1(),
        task_2(),
        task_3()
    )
    print('All tasks completed')
asyncio.run(main_3())
end = time.perf_counter()
print('Total time taken : ', end - start, ' seconds')

"""
Exercise 2 — Convert sync → async
Goal:
- See real difference between blocking and non-blocking

Task:
- Write synchronous version:
- 3 functions using time.sleep(2)
- measure total time
Write async version:
- same logic using asyncio.sleep(2)
- measure total time
✅ Expected learning:
- Sync ≈ 6 seconds
- Async ≈ 2 seconds
"""
start = time.perf_counter()
def function_1() :
    time.sleep(2)
    print('func_1')
def function_2() :
    time.sleep(2)
    print('func_2')
def function_3() :
    time.sleep(2)
    print('func_3')

function_1()
function_2()
function_3()
end = time.perf_counter()
print('Time taken for synchronous IO :', end - start, 'seconds')

start = time.perf_counter()

async def async_function_1():
    await asyncio.sleep(2)  # simulating I/O delay (like API call)
    print('func_1')

async def async_function_2():
    await asyncio.sleep(2)
    print('func_2')

async def async_function_3():
    await asyncio.sleep(2)
    print('func_3')

async def main_1():
    await asyncio.gather(
        # task=asyncio.create_task(function_1())
        async_function_1(),
        async_function_2(),
        async_function_3()
    )
asyncio.run(main_1())
end = time.perf_counter()
print('Time taken for asynchronous IO:', end - start, 'seconds')

"""
Exercise 3 — Async task manager
Goal:
- Work with multiple tasks dynamically

Task:
- Create a list of numbers: [1, 2, 3, 4, 5]
For each number:
- create an async function that:
- waits for n seconds
- prints: Task n done
- Run all tasks together using asyncio.gather()
🔥 Bonus:
Print:
- when task starts
- when task ends
✅ Expected learning:
- How to handle multiple async tasks
- How execution overlaps
"""
start = time.perf_counter()
lst = [1, 2, 3, 4, 5]

async def process_number(n):
    print(f"Start task {n}")
    await asyncio.sleep(n)   # make it interesting
    print(f"Task {n} done")

async def main():
    print("All tasks started")
    tasks = [process_number(n) for n in lst]
    await asyncio.gather(*tasks)
    print("All tasks completed")

asyncio.run(main())
end = time.perf_counter()
print("Time taken for AsyncIO:", end - start, "seconds")
"""
Exercise 4 — Real-world async (important)
Goal:
- Simulate real async I/O

Task:
- Create async function fetch_data(id)
- print: Fetching id
- wait random time (random.randint(1, 3))
- print: Done id
- Run 5–10 tasks together
🔥 Bonus (important):
- Measure total execution time
- Compare with synchronous version
If you want to push further (optional challenge)

👉 Modify Exercise 4:

- Limit number of concurrent tasks using:
- asyncio.Semaphore

This is real-world level concept (used in APIs, scraping, etc.)
"""
start = time.perf_counter()
async def fetch_data(task_id):
    print(f"fetching {task_id}...")
    await asyncio.sleep(2)
    print(f"done {task_id}")

async def main():
    await asyncio.gather(
        fetch_data(3424),
        fetch_data(2678),
        fetch_data(6878),
        fetch_data(4123),
        fetch_data(5798),
        fetch_data(6243),
        fetch_data(7890),
        fetch_data(8537),
        fetch_data(9888),
        fetch_data(1013)
    )
asyncio.run(main())
end = time.perf_counter()
print('Time taken for async I/O:', end - start, 'seconds')

"""
Async Project: Concurrent API Data Fetcher
Goal :

Build a system that:
- Fetches data from multiple APIs concurrently
- Handles delays
- Measures performance
- (later) handles failures
Step 1 : Setup
Install:
pip install aiohttp

Step 2 : Basic Version (Core Project)
import asyncio
import aiohttp
import time

start = time.perf_counter()

async def fetch_post(session, post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    print(f"Fetching post {post_id}...")
    
    async with session.get(url) as response:
        data = await response.json()
    
    print(f"Done post {post_id}")
    return data

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_post(session, i) for i in range(1, 11)
        ]

        results = await asyncio.gather(*tasks)

        print(f"\nFetched {len(results)} posts")

asyncio.run(main())

end = time.perf_counter()
print("Total time:", end - start, "seconds")
What this teaches us :
- Real async HTTP requests (not sleep)
- Task creation from loops
- Using session (important in real apps)
- Returning and collecting data

Step 3 : Compare with synchronous version
Write same logic using:

import requests

We’ll clearly see:
- Sync → slower
- Async → much faster

Step 4 : Add delay simulation
Add:
await asyncio.sleep(1)

=> Simulate real-world network latency

Step 5 : Handle errors (important upgrade)
Modify:
try:
    async with session.get(url) as response:
        data = await response.json()
except Exception as e:
    print(f"Error fetching {post_id}: {e}")
    return None
    
Step 6 : Limit concurrency (advanced)
Add:

semaphore = asyncio.Semaphore(3)

async def fetch_post(session, post_id):
    async with semaphore:
        ...

👉 Only 3 requests run at a time
👉 This is real production behavior
"""

"""
Purpose of this code :
                      Fetches data from 10 API endpoints at the same time instead of one by one.
"""
# -----------------------Async Version ---------------------------
start = time.perf_counter()
async def fetch_post(session, post_id, semaphore):
  async with semaphore:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    print(f"Fetching post {post_id}...")
    await asyncio.sleep(1)
    try :
       async with session.get(url) as response:
        data = await response.json()
        print(f"Done post {post_id}")
        return data    # each task return it's data

    except Exception as e:
        print(f"Error fetching {post_id}: {e}")
        return None
"""
session.get() → sends request
async with → handles connection properly
await response.json() → waits for data (non-blocking)
"""
async def async_main():
    semaphore = asyncio.Semaphore(5)
    async with aiohttp.ClientSession() as session: # it'll create a session
        tasks = [
            fetch_post(session, i, semaphore) for i in range(1, 11) # it'll create 10 coroutine objects
        ]

        results = await asyncio.gather(*tasks) # starts all tasks together - waits for all to finish - collects results in a list

        print(f"\n[ASYNC] Fetched {len(results)} posts")

asyncio.run(async_main())

end = time.perf_counter()
print("[ASYNC] Total time:", end - start, "seconds")

# -------------------- Synchronous version --------------------------------
start = time.perf_counter()
def sync_fetch_post(session, post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    print(f"Fetching post {post_id}...")

    response = session.get(url)
    data = response.json()
    print(f"Done post {post_id}")
    return data

def main():
    results = []
    session = requests.Session()  # ✅ create session
    for i in range(1, 11):
        result = sync_fetch_post(session, i)  # runs one by one
        results.append(result)
    print(f"\n[SYNC] Fetched {len(results)} posts")
main()
end = time.perf_counter()
print(" [SYNC] Total time:", end - start, "seconds")