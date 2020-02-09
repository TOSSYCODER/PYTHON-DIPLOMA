import requests_html
from requests_html import HTMLSession, HTMLResponse

session = HTMLSession()

response = session.get('http://172.16.104.50/').html

#print(response)

#block = response.find('.article')[0]

# for i in range (0,9):
#     print(block[i].text)

#print(block.text)

# headline = block.find('h2')[0]
# print(headline.text)

# summary = block.find('p')[0]
# print(summary.text)
tittle = response.find('h1')
print(tittle[0].text)
print()



blocks = response.find('.article')
blocksr = response.find('#test')

headlines = []
headlinesr = []
summaries = []
summariesr = []

# for block in blocks:
#     headline = block.find('h2')[0]
#     print(headline.text)
    
#     summary = block.find('p')[0]
#     print(summary.text)
    

for block in blocks:
    headline = block.find('h2')[0]
    #print(headline.text)
    headlines.append(headline.text)

    summary = block.find('p')[0]
    #print(summary.text)
    summaries.append(summary.text)

for blockr in blocksr:
    headliner = blockr.find('h2')[0]
    headlinesr.append(headliner.text)

    summaryr = block.find('p')[0]
    summariesr.append(summaryr.text)





print(headlines)
print()
print(summaries)
print()
print(headlinesr)
print()
print(summariesr)
print()

response.render()

footer = response.find('#footer')[0]
paras = footer.find('p')

for para in paras:
    print(para.text)
print()