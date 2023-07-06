'''
[
    {
        'link' : 'url',
        'title' : 'header'
        'text' : [p1, p2, p3]
    }
]
'''

import requests
from bs4 import BeautifulSoup






def parse_european_news(date=None):
    links = []
    result = []
    if date is None:
        response = requests.get('https://www.eurointegration.com.ua/')
        soup = BeautifulSoup(response.content, 'html.parser')

        headers = soup.select('.article__title > a')
        
        # print(headers[:3])
        
        for link in headers[:3]:
             l = link.get('href')
             result_links = l if l[0:5] == 'https' else 'https://www.eurointegration.com.ua/' + l 
             links.append(result_links)
        

        # print(links)


        for link in links:
             link_response = requests.get(link)
             link_soup = BeautifulSoup(link_response.content, 'html.parser' )

            

        # print(link_soup)
        

             title = link_soup.select_one('.post__title').text
            #  print(title)
            
        
             texts = link_soup.select('.post__text > p')

            #  print(texts)
        



             news_body = []

             for i in texts:
                 article_text = i.text
                 news_body.append(f'{article_text}\n')

            #  print(news_body)


             article_body = ''.join(news_body)


            #  print(article_body)
             
            
             result.append(
                 {
                     'link' : link,
                     'title' : title,
                     'text' : article_body
                 }
             )

            #  print(result)
        
        return result
            
            
            
            

def parse_economical_news(date=None):
    links = []
    result = []
    if not date:
        response = requests.get('https://www.epravda.com.ua/')
        soup = BeautifulSoup(response.content, 'html.parser')

        headers = soup.select('.article__title > a')

        for link in headers[:3]:
            l = link.get('href')
            
            result_links = l if l[0:5] == 'https' else 'https://www.epravda.com.ua/' + l
            links.append(result_links)



        # print(links)


        for link in links:
            link_response = requests.get(link)
            link_soup = BeautifulSoup(link_response.content, 'html.parser')

            title = link_soup.select_one('.post__title').text

            # print(title)

            texts = link_soup.select('.post__text > p')
            # print(texts)



            news_body = []

            for i in texts:
                article_text = i.text
                news_body.append(f'{article_text}\n')


            article_body = ''.join(news_body)
            


       
            result.append(
                {
                    'link' : link,
                    'title' : title,
                    'text' : article_body
                }
            )
        
        return result







if __name__ == '__main__':
    print(parse_economical_news())