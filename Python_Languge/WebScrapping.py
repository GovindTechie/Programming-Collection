#Perform Web Scraping to fetch the data from Website URL (Wikipedia) using Python Libraries.



import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and print the title of the page
title = soup.title.string
print(f"Title: {title}")

# Extract all paragraphs
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())