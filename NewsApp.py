"""
Exercise 10: News App in Python
Author: Shahroze
Date: 2026-03-16
Description:
    This Python application uses the NewsAPI and the requests module
    to fetch the latest news articles. Users can:
      1. Search for news by topic using the /v2/everything endpoint.
      2. Fetch the latest headlines from a specific source (BBC News)
         using the /v2/top-headlines endpoint.
Notes:
    - Categories available for top-headlines: business, entertainment,
      general, health, science, sports, technology.
    - For topic-specific searches like AI or cryptocurrency, use the 'q' parameter.
    - API key is required from https://newsapi.org/
"""
"""
Exercse 10 : News app in python
=> Use the NewsAPI and the requests module to fetch the daily news related to different topics.
=> Go to : https://newsapi.org/
=> Explore various options to build you application.
"""
import os
import requests
os.system('cls')
interested_topic = input(f' Enter topic :  ') 
url = 'https://newsapi.org/v2/everything' # here we use 2 things url : https://newsapi.org/ endpoint : v2/top-headlines
params = {"q" : interested_topic, 'language' : 'en', 'pageSize' : 5 , 'apiKey' : 'bd398caceb8c4c339f4a0b3d86cd2cc7'} # q means query.
response = requests.get(url, params = params)
# print(response.json())
data = response.json()

for article in data["articles"]:
    print("\nTitle:", article["title"])
    print("Source:", article["source"]["name"])
    print("URL:", article["url"])

# For a specific source from newsapi
print('Fetching news from BBC News ...')
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'sources' : 'bbc-news', # source id
    'pageSize' : 4,
    'apiKey' : 'bd398caceb8c4c339f4a0b3d86cd2cc7'
}
response = requests.get(url , params = params)
data = response.json()

for article in data["articles"]:
    print("\nTitle:", article["title"])
    print("URL:", article["url"])
# In NewsAPI, the categories are fixed. You can use them in the category parameter with /v2/top-headlines (not /v2/everything).
# Here are all the categories:
# => business
# => entertainment
# => general
# => health
# => science
# => sports
# => technology

# Note : 
# - You cannot create custom categories like “Petrol prices” or “Artificial Intelligence” .
# - To search for specific topics (like AI or crypto), use the q parameter with the /v2/everything endpoint instead of category.