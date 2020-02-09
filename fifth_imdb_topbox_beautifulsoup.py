import requests_html
import csv
from requests_html import HTMLSession,HTMLResponse
from bs4 import BeautifulSoup

csv_file = open('IMDB_TOPBOX(US).csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['TITLE', 'WEEKEND', 'CROSS', 'WEEK','COVER URL'])

session = HTMLSession()

link = 'https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'
tittle_li = []
cover_li = []
weekend_li = []
cross_li = []
weeks_li = []

response = session.get(link).html
source = response.html
# print(source)
soup = BeautifulSoup(source, 'lxml')

box = soup.find('tbody')
# print(box.text)


elements = box.find_all('tr')
# print(element.text)

for element in elements:
    tittle = element.select('td a')[1]
    # print(tittle.text)
    tittle_li.append(tittle.text)

    weekend = element.find('td', class_='ratingColumn')
    # print(weekend.text)
    # w = weekend.text.split('\n                    ')
    # w1 = w[1].split('        ')
    weekend_li.append(weekend.text.strip())

    cover = element.select('a img')[0]['src']
    # print(cover)
    cover_li.append(cover)

    cross = element.find('span', class_='secondaryInfo')
    # print(cross.text)
    cross_li.append(cross.text)

    week = element.find('td', class_='weeksColumn')
    # print(week.text)
    weeks_li.append(week.text)

    csv_writer.writerow([tittle.text, weekend.text.strip(), cross.text, week.text, cover])

print('MOVIE TITLE:',tittle_li)
print()
print('COVER: ',cover_li)
print()
print('WEEKEND:',weekend_li)
print()
print('CROSS:',cross_li)
print()
print('WEEKS:',weeks_li)

csv_file.close()