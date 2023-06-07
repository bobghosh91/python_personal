import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('article')

for article in articles:
    headline = article.find('h3').text.strip()
    link = article.find('a')['href']
    print(headline)
    print(link)
    print('---')