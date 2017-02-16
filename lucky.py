#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(3, len(linkElems))
hrefVector = []
for i in range(numOpen):
	oneHref = linkElems[i].get('href')
#    webbrowser.open('http://google.com' + oneHref)
	hrefVector.append(oneHref)
#    webbrowser.open('http://google.com' + linkElems[i].get('href'))

for i in range(len(hrefVector)):
	print(hrefVector[i] + '\n')
	


