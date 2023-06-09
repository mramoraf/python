import requests
from bs4 import BeautifulSoup




response = requests.get('http://start.karazin.ua/page/dopushcheni#reiting#')
soup = BeautifulSoup(response.content, 'html.parser')

# for row in soup.select('.right-nav.table-cell.ic-evaluation > .item > a'):
#     print(f"{row.text} - {row.get('href')}")
    


with open('semester 2\\class 10\\classwork\\links.txt', 'w', encoding="utf-8") as file:
    for row in soup.select('.right-nav.table-cell.ic-evaluation > .item > a'):
        b = f"{row.text} - {row.get('href')}\n"
        file.write(b)


