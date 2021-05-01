import os
import zipfile
import sys
import csv

print("Hello " + str(os.getlogin()) + "!")
print("You are using the ett_create script from the BELDUM package ",
    "for Pokémon VGC competitions data analysis.\n")

print("Extracting form data", end="")
archive = zipfile.ZipFile("raw.csv.zip", "r")
archive.extractall()
print("...done!\n")

file = open("raw.csv", "r")
reader = csv.reader(file)

#################################################
#Reading infos and creating the INFO.txt file

print("We are going to select the other INFOs beyond the ETTs.")
print("How many infos (i.e. question in the form) you want to consider?",
        "Do not take into account the ETT text box.")

info_keys = []
n_infos = int(input("Enter the n. of additonal infos: "))
for col in range(2, 2 + n_infos): #Starting from ETT column + 1
    info_key = input("Enter the key name of the {} info: ".format(col-1))
    info_keys.append(info_key)

########################################################
#Modify the teams adding the infos.

archive = zipfile.ZipFile("teams.zip", "r")
print("N. of teams: " + str(len(archive.namelist())))
archive.extractall()
teamlist = archive.namelist()

print("Adding INFOs in the team files", end="")
i = 0
next(reader)
for team, row in zip(teamlist, reader):
    f = open(team, "a")
    f.write("\n")
    f.write("### INFOs START HERE ###\n")
    f.write("\n")
    for key, col in zip(info_keys, range(2, n_infos + 2)):
        line = key + ": " + row[col]
        f.write(line)
    f.write("\n")
    f.close()

########################################################
#Re-zip teams file and delete the extracted ones

new_archive = zipfile.ZipFile("teams_up.zip", "w")
for team in teamlist:
    new_archive.write(team)
    os.remove(team)

new_archive.close()   

########################################################

print("...done!\n")
os.system("pause")