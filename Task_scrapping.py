from bs4 import BeautifulSoup
import requests

xml_text = requests.get('https://wiadomosci.onet.pl/9,sitemap-news.xml').text
soup = BeautifulSoup(xml_text, 'lxml-xml')
url = soup.find_all('loc')


def get_articles():
    articles = dict()
    for index, single in enumerate(url):
        article = requests.get(f'{single.text}').text
        parsed_article = BeautifulSoup(article, 'lxml')
        title = parsed_article.find('h1', class_='mainTitle').text
        abstract = parsed_article.find(id='lead').text
        date = parsed_article.find('span', class_='datePublishedContent').text
        try:
            author = parsed_article.find('span', class_='authorItemName').text
        except AttributeError:
            author = 'None'

        articles[f'Article {index+1}'] = {'Title': title.strip('\n '),
                                          'Abstract': abstract,
                                          'Date': date,
                                          'Author': author,
                                          }
        if index == 4:
            break
    return articles

