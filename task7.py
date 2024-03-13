# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 7 Web Scraping
# done by Sora
# Write a Python program that scrapes the titles of the top 5 news articles from a news website (e.g., BBC News) using the requests and BeautifulSoup libraries.

import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

# URL of the news website
URL = 'https://www.bbc.com/news'

# send a GET request to the URL and create a BeautifulSoup object
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
response.raise_for_status()  # Raise an HTTPError for bad responses

# find the container with the latest news stories
results = soup.find(id="latest-stories-tab-container")

# find all the article titles within the container
article_title = results.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")

# print the top 5 news titles
print("Top 5 News Titles:")
for i, title in enumerate(article_title[:5], start=1):
    print(f"{i}. {title.text.strip()}") # print the formatted title


