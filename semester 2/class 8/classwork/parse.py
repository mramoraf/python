from bs4 import BeautifulSoup

with open('D:\\go iteens\\semester 2\\class 8\\classwork\\films.html') as file:
    soup = BeautifulSoup(file, "html.parser")


# for data in soup.find_all('h3'): 
#     print(data.text)

# for data in soup.select('.genre, .year, .country'):
#     print(data.text)


# for data in soup.select('.header > h1'):
#     print(data.text)

# div = soup.select_one('.header > h1')
# print(div.text)


div2 = soup.find(id='2')
print(div2.text.strip())