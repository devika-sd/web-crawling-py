from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("file:///home/devika/Desktop/steak/menu.html")
tags=html.read()
bsob=BeautifulSoup(tags,"html.parser")
print(bsob.h1)
