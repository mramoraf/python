from bs4 import BeautifulSoup

with open('semester 2\\class 8\\homework\\info.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

for data in soup.find_all('ol'):
    print(data.text.strip())

for data in soup.find_all('ul'):
    print(data.text.strip())
          