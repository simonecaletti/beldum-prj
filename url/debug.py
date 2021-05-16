import os
import sys
import urllib.request as url #For point (1)
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import csv
from time import sleep
import zipfile

##############################################################################
# Write an ett from a pokepaste link

def get_ett(paste, filepath):
    # Convert HTML in pandas DataFrame using Web scraping
    page = get(paste)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    #print(body)

    # Open txt file and write ett
    outFile = open(filepath, 'w+', encoding='utf-8')

    # print(body) #ETT infos are contained in the body of a pokepaste
    for pkm in body.find_all('pre'):
        print(list(pkm.children))
        if any(["span class" in  x for x in list(pkm.children)]):
            if pkm != body.find_all('pre')[0]:
                outFile.write("\n")
            outFile.write(pkm.get_text()[:-1]) #This is precisely a Pokemon is all it's ok
        else:
            outFile.write(pkm.get_text().replace("\n","")) #If problems
            outFile.write("\n")
        outFile.write("---------------\n")

#########################################################################
# MAIN

#         [funziona, rotto]
links = ["https://pokepast.es/9ba8fc07d08c9a2d", "https://pokepast.es/ee229428b0a697df", "https://pokepast.es/14781ecedd0314c1"]
filenames = ["team1.txt", "team2.txt", "team11.txt"]
for paste, name in zip(links, filenames):
    print("Extraction...done!")
    get_ett(paste, name)
