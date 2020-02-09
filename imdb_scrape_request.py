import requests_html
from requests_html import HTMLSession, HTMLResponse

session = HTMLSession()

response = session.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').html

body = response.find('.lister-list')[0]
#print(body)

# block = body.find('tr')[0]
# #print(block)

# tab = block.find('.titleColumn a')[0]
# print(tab.text)

# rating = block.find('td.ratingColumn.imdbRating')[0]
# print(rating.text)

blocks = body.find('tr')
#print(block)
i = 0
for block in blocks:
    i = i+1
    print("MOVIE NO.:",i)
    tab = block.find('.titleColumn a')[0]
    print("TITTLE:",tab.text)

    rating = block.find('td.ratingColumn.imdbRating')[0]
    if rating.text == "":
        print("NOT RELEASED YET!")
        print()
        continue
    print("RATINGS:",rating.text,"/10")
    print()
