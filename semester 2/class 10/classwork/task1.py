import requests
from bs4 import BeautifulSoup


response = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(response.content, 'html.parser')

with open('semester 2\\class 10\\classwork\\books.txt', 'w') as file:
    for i in soup.select('.col-xs-6.col-sm-4.col-md-3.col-lg-3 > .product_pod > h3 > a'):
        a = f"{i.get('title')} --- {i.get('href')}\n"
        file.write(a)

