import requests
from bs4 import BeautifulSoup


response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')




for posts in soup.select('.text'):
    for author in soup.select('.author'):
        print(posts.text, '--', author.text)
    