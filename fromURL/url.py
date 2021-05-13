import os
import sys
import urllib.request as url #For point (1)
import pandas as pd
from bs4 import BeautifulSoup

# #(1) Read HTML pages line by line
# data = url.urlopen("https://pokepast.es/e6ccdce63b42a0ba")
# for line in data:
#     print(line.decode('utf-8'))

# (2) Convert HTML in pandas DataFrame
path = "prova.html"
data = []
list_header = []

soup = BeautifulSoup(open(path), 'html.parser')
header = soup.find_all("table")[0].find("class")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = soup.find_all("table")[0].find_all("class")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

dataframe = pd.DataFrame(data = data, columns = list_header)
dataframe.to_csv('prova.csv')