import requests
import bs4 
#from bs4 import BeautifulSoup
#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#print(res.text)

exampleFile = open('example.html')
readed = exampleFile.read()
exampleSoup = bs4.BeautifulSoup(readed)
#type(exampleSoup)

#noStarchSoup = bs4.BeautifulSoup(res.text)
#type(noStarchSoup)


