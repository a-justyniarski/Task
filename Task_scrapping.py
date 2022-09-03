from bs4 import BeautifulSoup
import requests

ADDRESS = 'https://wiadomosci.onet.pl/9,sitemap-news.xml'


def get_articles(address):
    '''
    Funcion downloads xml from onet site and returns dictionary with data (title, abstract, date,
     and author) of 5 latest articles.
    :return:
    '''
    xml_text = requests.get(address).text
    soup = BeautifulSoup(xml_text, 'lxml-xml')
    url = soup.find_all('loc')
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



if __name__ == "__main__":
    get_articles(ADDRESS)
