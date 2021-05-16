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
        if "span class" in str(list(pkm.children)[0]):
            if pkm != body.find_all('pre')[0]:
                outFile.write("\n")
            outFile.write(pkm.get_text()[:-1]) #This is precisely a Pokemon is all it's ok
        else:
            outFile.write(pkm.get_text().replace("\n","")) #If problems
            outFile.write("\n")
        #outFile.write("---------------\n")
    
#########################################################################
# MAIN

print("Hello " + str(os.getlogin()) + "!")
print("You are using the from_url script from the BELDUM package ",
    "for Pokémon VGC competitions data analysis.\n")

#Create team folder if do not exist
#if not os.path.exists("teams"):
#    os.mkdir("teams")

#Remove old zip file
if os.path.exists("teams.zip"):
    os.remove("teams.zip")
archive = zipfile.ZipFile("teams.zip", "w")

raw = open("raw.csv", "r")
reader = csv.reader(raw)
next(reader)

print("N. of teams will be downloaded: " + str(len(list(reader))))
ans = input("Do you want to continue? [y/n]: ")
if ans != 'y':
    sys.exit()

i=1
col = -1 #Select the column with the link
for row in reader:
    paste = row[col]
    filename = "team" + str(i) + ".txt"
    print("Extracting " + str(i) + "...", end="")
    get_ett(paste, filename)
    print("done!")

    
    archive.write(filename)
    os.remove(filename)

    sleep(0.1)
    i += 1

archive.close()

#os.system('pause')