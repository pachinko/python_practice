import requests
import bs4 
#from bs4 import BeautifulSoup
#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#print(res.text)

exampleFile = open('example.html')
readed = exampleFile.read()
exampleSoup = bs4.BeautifulSoup(readed)
elems = exampleSoup.select('#author')
#print("Elems: ", elems)
print(elems)

#print(elems[0].getText() )
#print(str(elems[0]) )
#print(elems[0].attrs )
#type(exampleSoup)

#noStarchSoup = bs4.BeautifulSoup(res.text)
#type(noStarchSoup)
pElems = exampleSoup.select('p')
print(str(pElems[0]) )
print( pElems[0].getText() )



