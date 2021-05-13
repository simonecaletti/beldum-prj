import os
import sys
import urllib.request as url #For point (1)
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import csv
from time import sleep

##############################################################################
# Write an ett from a pokepaste link

def get_ett(paste, filepath):
    # Convert HTML in pandas DataFrame using Web scraping
    page = get(paste)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]

    # Open txt file and write ett
    outFile = open(filepath, 'w+', encoding='utf-8')

    # print(body) #ETT infos are contained in the body of a pokepaste
    for pkm in body.find_all('pre'):
        outFile.write(pkm.get_text()) #This is precisely a Pokemon
    
#########################################################################
# MAIN

#Create team folder if do not exist
if not os.path.exists("teams"):
    os.mkdir("teams")

raw = open("battlefy-palace.csv", "r")
reader = csv.reader(raw)
next(reader)

i=1
col = -1 #Select the column with the link
for row in reader:
    paste = row[col]
    filename = "team" + str(i) + ".txt"
    filepath = "teams/" + filename
    print("Extracting " + str(i) + "...", end="")
    get_ett(paste, filepath)
    print("done!")
    i += 1

    sleep(0.1)