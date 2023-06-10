import requests
from bs4 import BeautifulSoup


response = requests.get('https://univ.kiev.ua/ua/departments')
soup = BeautifulSoup(response.content, 'html.parser')

for i in soup.select_one('.b-references > .b-references__holder'):
    print(i.text.strip())





