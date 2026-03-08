"""
requests_module.py

This script contains practice exercises for Python's requests module, covering:
- GET and POST requests
- Sending data and query parameters
- Working with JSON responses
- Using custom headers
- Checking response status codes
- Downloading files (PDFs and images)

Author: Shahroze
"""

"""
The requests module in Python is used to send HTTP requests to websites and web services, 
allowing a Python program to communicate with servers over the internet.

What is an HTTP request?

When you visit a website, your browser sends a 'request' to the website's server, asking for a page. 
The server then 'responds' with the webpage's content. This communication follows the HTTP (HyperText Transfer Protocol). 
The requests module allows Python programs to do the same communication programmatically.

Why use requests?

=> To fetch data from a website or APIs(like downloading a webpage or API data).
=> To send data servers (like submitting a form or logging in).
=> To interact with web services (like getting weather data, stock prices, etc.).


Common Types of Requests :
1. GET Request – Used to request data from a website.
2. POST Request – Used to send data to a website.
3. PUT Request – Used to update existing data.
4. DELETE Request – Used to delete data.
5. PATCH Request - partially update data
6. HEAD Request - Get headers only

In real ML / data work, these are the most common:

=> requests.get()
=> response.json()
=> params
=> headers
=> checking status_code 

These are used when working with APIs, datasets, cloud services, and web data.

status_code shows the HTTP response code returned by the server, indicating whether the request was successful or if an error occurred.

Common Status Codes : 
Code	Meaning
200	    OK – request successful
201	    Created – something was successfully created (often after POST)
400	    Bad Request – the request was incorrect
401	    Unauthorized – authentication required
403	    Forbidden – access denied
404	    Not Found – resource doesn't exist
500	    Internal Server Error – problem on the server

import requests
response = requests.get("https://api.github.com")

print(response.status_code)

✅ Best practice site overall:
httpbin → APIs
FileExamples → file downloads
JSONPlaceholder → JSON APIs
"""
# 1. Sending a GET Request - Used to retrieve data from a website or API.
import requests
response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)

# status_code tells if the request succeeded (200 means success).

# 2. Sending a POST Request - Used to send data to a server (forms, APIs, login).
# import requests
data = {"username": "john", "password": "123"}
response = requests.post("https://example.com/login", data=data)

print(response.status_code)

# 3. Working with JSON Data - Most APIs return JSON data.
response = requests.get("https://api.github.com")
data = response.json()
print(data)
# .json() converts the response into a Python dictionary.

# 4. Sending Parameters in a URL - Used when APIs require query parameters.

# URL:
# https://httpbin.org/get
# Python version:
params = {"id": 10}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)

# 5. Checking Response Status - Always check if the request succeeded.
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    print("Request successful")
else:
    print("Request failed")

# 6. Request Headers - Sometimes APIs require headers (authentication, tokens, etc.).
headers = {"User-Agent": "my-app"}

response = requests.get("https://restcountries.com/v3.1/name/USA", headers=headers)
print(response.status_code)
# Headers	                                     Access
# Sent by you (request)	                 response.request.headers
# Sent by server (response)	             response.headers

# 7. Downloading Files - requests can download files like images or PDFs.
# practice site : FileExamples
url = "https://file-examples.com/wp-content/uploads/2017/10/file-example_PDF_1MB.pdf"
response = requests.get(url)
with open("file.pdf", "wb") as f:
    f.write(response.content)
    print('File downloaded successfully')

# wb means write binary, needed for files.
""" 
Note : 
Files you download using requests will go to Colab’s virtual machine storage (usually under /content).
You cannot directly see them on your local PC unless you download them manually from Colab.
"""

# query parameters with multiple values

params = {"userId": 1, "id": 5}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.json())

# Experiment with POST requests on a testing API
# https://httpbin.org/post can safely accept POST data, and you can inspect what was sent.
data = {"name": "Shahroze", "role": "ML"}
response = requests.post("https://httpbin.org/post", data=data)
print(response.json())

# Use custom headers to mimic a browser
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get("https://httpbin.org/get", headers=headers)
print(response.json())

# Practice downloading images and verifying content size
url = "https://httpbin.org/image/png"
response = requests.get(url)
with open("image.png", "wb") as f:
    f.write(response.content)
print("Downloaded image size:", len(response.content), "bytes")