from bs4 import BeautifulSoup
import requests

response = requests.get('http://yermilovcentre.org/medias/')
soup = BeautifulSoup(response.content, 'html.parser')

for i in soup.select(' .col-6.mx-0.no-gutters.row.mt-0.mt-n2 > a'):
    result = f"{i.text.strip()} -- {i.get('href')}"
    print(result)





