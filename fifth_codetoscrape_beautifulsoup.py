import requests_html
import csv
from requests_html import HTMLSession,HTMLResponse
from bs4 import BeautifulSoup

csv_file = open('QUOTES_TO_SCRAPE.csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['QUOTES','AUTHORS', 'TAGS'])
session = HTMLSession()

link = 'http://quotes.toscrape.com/'
quotes_li = []
authors_li = []
tags_li = []
urls = []
# c = 0
# p = 0

for i in range(1,11):
    urls.append(link + 'page/'+ str(i) +'/')
    # print(urls)

for url in urls:
    # p=p+1
    # print('PAGE NO.: ',p)
    response = session.get(url).html
    source = response.html
    soup = BeautifulSoup(source, 'lxml')
    # for j in range(0,2):
    
    # c=c+1
    boxes = soup.find_all('div', class_='quote')
    for box in boxes:
        # c=c+1
        # print(box.text)
        # elements = box.find('div', class_='quote')
        # print(elements.text)
        # for element in elements:
        # for j in range (0,2):
        quote = box.find('span', class_='text')
        # print("QUOTE NO.:",c)
        author = box.find('small')
        # print(author.text)
        tags = box.find_all('a', class_='tag')
        for tag in tags:
            tags_li.append(tag.text)
        # print(tags.text)
        authors_li.append(author.text)
        # print(quote.text)
        quotes_li.append(quote.text)
        # print()

        csv_writer.writerow([quote.text, author.text, tag.text])

print(quotes_li)
print()
print(authors_li)
print()
print(tags_li)

csv_file.close()