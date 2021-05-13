import os
import sys
import urllib.request as url #For point (1)
import pandas as pd
from bs4 import BeautifulSoup
from requests import get

# #(1) Read HTML pages line by line
# data = url.urlopen("https://pokepast.es/e6ccdce63b42a0ba")
# for line in data:
#     print(line.decode('utf-8'))

# (2) Convert HTML in pandas DataFrame using Web scraping
page = get("https://pokepast.es/e6ccdce63b42a0ba")
soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[2]
body = list(html.children)[3]

#Open txt file and write ett
outFile = open("ett.txt", 'w+')

#print(body) #ETT infos are contained in the body of a pokepaste
for pkm in body.find_all('pre'):
    outFile.write(pkm.get_text()) #This is precisely a Pokemon