import requests
from bs4 import BeautifulSoup

response = requests.get('https://shop.karazin.ua/kantselyariya/')
soup = BeautifulSoup(response.content, 'html.parser')

# for i in soup.select('.catalogCard-title > a'):
#     for b in soup.select('.catalogCard-price'):
#         print(f"{i.get('title')} -- {b.text}")



for i in soup.select('.catalogCard-info'):
    a = i.text.strip()
    print(a)