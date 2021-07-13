#! python3
# searchpypi.py - Opens several search results.
# Updated by SeungWon Bae

import requests, sys, webbrowser, bs4
# import os

print('Searching...')   # display text while downloading the search result page

# addr = 'https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])
addr = 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])

# print(addr)

res = requests.get(addr)
res.raise_for_status()

# # print(res.text)
# # save the result to HTML file
# resFile = open('searchResult.html', 'wb')
# for chunk in res.iter_content(100000):
#     # print(chunk)
#     resFile.write(chunk)
# resFile.close()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
linkElems = soup.select('.package-snippet')
# linkElems = soup.select('.kCrYT a')
# linkElems = soup.select('.yuRUbf a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)