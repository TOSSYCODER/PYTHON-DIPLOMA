import requests_html
from requests_html import HTMLSession, HTMLResponse

session = HTMLSession()

response = session.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html
#print(response)
print(type(response))
for i in range (0,2):
    body = response.find('div.list.detail.sub-list')[i]
    # print(body.text)

    blocks = body.find('.nm-title-overview-widget-layout')
    # print(blocks)

    i = 0
    for block in blocks:
        i = i+1
        print("MOVIE NO.:",i)
        tab = block.find('.overview-top a')[0]
        print("TITTLE:",tab.text)

        # rating = block.find('span.metascore.mixed')[0]
        # if rating.text == "":
            # print("NOT RELEASED YET!")
            # print()
            # continue
        # print("METASCORE:",rating.text)
        # print()

        runtime = block.find('time')[0]
        print("RUNTIME:",runtime.text)

        plot = block.find('.outline')[0]
        print("PLOT:",plot.text)

        directorr = block.find('div.txt-block')[0]
        d = directorr.text.split('|')
        dd = d[0].split('\n')
        d[0] = dd[1]
        print("DIRECTORS:",end=' ')
        for b in d:
            print(b,end=' ')

        print()
        print()
# a = response.html
# print(a)
# print(type(a))
