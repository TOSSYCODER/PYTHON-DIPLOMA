import requests_html
import csv
from requests_html import HTMLSession,HTMLResponse
from bs4 import BeautifulSoup

csv_file = open('BOOKS_TO_SCRAPE.csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['BOOK TITLE','BOOK PRICE', 'BOOK COVER URL'])

session = HTMLSession()

link = 'http://books.toscrape.com/'
tittle_li = []
price_li = []
image_link_li = []
urls = []

for i in range(1,51):
    urls.append(link + 'catalogue/page-'+ str(i) + '.html')

for url in urls:
    response = session.get(url).html
    source = response.html
    # print(response)
    # print(source)

    soup = BeautifulSoup(source, 'lxml')
    # print(type(soup))

    box = soup.find('ol')
    # print(type(box))

    elements = box.find_all('li')
    # print(type(element))
    # print(element)

    for element in elements:
        tittle = element.select('h3 a')[0]['title']
        # print('BOOK TITTLE:',tittle)
        tittle_li.append(tittle)

        price = element.find('p', class_='price_color')
        # print('PRICE:',price.text)
        price_li.append(price.text)

        image = element.find('img')['src']
        image_url = link+image
        # print('BOOK COVER LINK:',image_url)
        image_link_li.append(image_url)

        csv_writer.writerow([tittle, price.text, image_url])

print('BOOKS TITLES: ')
print(tittle_li)
print()
print('BOOKS PRICES: ')
print(price_li)
print()
print('BOOKS COVER PAGE LINK: ')
print(image_link_li)
print()

csv_file.close()