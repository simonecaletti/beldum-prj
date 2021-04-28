import os
import zipfile
import sys
import csv

print("Hello " + str(os.getlogin()) + "!")
print("You are using the zip_create script of the BELDUM package ",
    "Pokemon VGC competition data analysis. ",
    "Enjoy this tool but be sure to cite Simone Caletti (aka Manabu) if ",
    "you want to share your results.\n")

print("Extracting form data", end="")
archive = zipfile.ZipFile("raw.csv.zip", "r")
archive.extractall()
print("...done!\n")

file = open("raw.csv", "r")
reader = csv.reader(file)


#################################################
#Create ETT in txt format

print("We are going to select the ETT only.",
    "All other infos collected by the form will be neglected.\n")

print("Creating ETT files", end="")
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
print("...done!\n")
#############################################
#Zip them in an archive

os.remove("team0.txt")

print("Storing all ETTs in a zip file", end="")
if os.path.exists("teams.zip"):
    os.remove("teams.zip")

new_archive = zipfile.ZipFile("teams.zip", "w")
 
for j in range(1, i):
    teamname = "team" + str(j) + ".txt"
    new_archive.write(teamname)
    os.remove(teamname)

new_archive.close()
print("...done!\n")

os.system("pause")


