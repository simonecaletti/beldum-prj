import os
import sys
import urllib.request as url

data = url.urlopen("https://pokepast.es/e6ccdce63b42a0ba")
for line in data:
    print(line.decode('utf-8'))