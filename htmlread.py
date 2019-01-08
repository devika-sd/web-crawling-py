from urllib.request import urlopen
html=urlopen("file:///C:/Users/Devika/Downloads/steak/steak/menu.html")
print(html.read())
