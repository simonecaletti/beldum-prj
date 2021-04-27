import os
import zipfile
import sys
import csv

archive = zipfile.ZipFile("raw.csv.zip", "r")
archive.extractall()

file = open("raw.csv", "r")
reader = csv.reader(file)


#################################################
#Create ETT in txt format

i = 0
col = 1 #Select the column with the team
#we cut away the score for the moment
for row in reader:
    #print(row[col])
    teamname = "team" + str(i) + ".txt"
    team = open(teamname, "a")
    team.write(row[col])
    team.close()

    i += 1

#############################################
#Zip them in an archive

os.remove("team0.txt")

if os.path.exists("teams.zip"):
    os.remove("teams.zip")

new_archive = zipfile.ZipFile("teams.zip", "w")
 
for j in range(1, i):
    teamname = "team" + str(j) + ".txt"
    new_archive.write(teamname)
    os.remove(teamname)

new_archive.close()
    




