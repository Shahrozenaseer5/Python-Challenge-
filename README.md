" Async vs Sync API Data Fetcher "

Overview :

This project demonstrates the difference between synchronous and asynchronous I/O operations in Python by fetching data from a public API.

The asynchronous version uses asyncio and aiohttp to perform multiple API requests concurrently, while the synchronous version uses requests to execute them sequentially.

Objectives :
- Understand blocking vs non-blocking execution
- Learn how asyncio works in real scenarios
- Compare performance between sync and async approaches
- Implement concurrency control using semaphores

Key Concepts Covered :
- async / await
- Event loop
- asyncio.gather()
- Concurrent task execution
- aiohttp.ClientSession
- Error handling in async code
- Concurrency limiting using asyncio.Semaphore

⚙️ Technologies Used :
- Python
- asyncio
- aiohttp
- requests
- time

📂 Project Structure
project/
│
├── main.py          # Contains both async and sync implementations
├── README.md        # Project documentation
🔄 How It Works
Asynchronous Version :
- Sends multiple API requests concurrently
- Uses asyncio + aiohttp
- Limits concurrency using Semaphore

Synchronous Version :
- Sends API requests one by one
- Uses requests
- Blocks execution until each request completes

⏱ Performance Comparison
Approach	             Execution	             StyleExpected Time
Asynchronous	         Concurrent	              ~2–4 seconds
Synchronous	             Sequential	              ~8–12 seconds

Note: Time may vary depending on network conditions.

▶️ How to Run
1. Install dependencies
pip install aiohttp,  requests
2. Run the script
python main.py
📊 Example Output
[ASYNC] Fetched 10 posts
[ASYNC] Total time: 3.2 seconds

========================================

[SYNC] Fetched 10 posts
[SYNC] Total time: 9.8 seconds
Key Insight :

Asynchronous programming improves performance by allowing multiple I/O operations to run concurrently instead of waiting for each one to finish.

Future Improvements :
- Add retry mechanism for failed requests
- Implement timeout handling
- Save fetched data to JSON file
- Add logging instead of print statements
👤 Author :
           Shahroze
Aspiring Machine Learning Engineer