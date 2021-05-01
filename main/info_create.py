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
#Extract infos and create the INFO.txt files

print("We are going to select the other INFOs beyond the ETTs.")
print("How many infos (i.e. question in the form) you want to consider?",
        "Do not take into account the ETT text box.")

n_infos = int(input("Enter the n. of additonal infos: "))
infos = []
for col in range(2, 2 + n_infos): #Starting from ETT column + 1
    if col == 2:
        infos.append(input("Enter the key name of the {} info: ".format(col-2)))
    else:
        infos.append("," + input("Enter the key name of the {} info: ".format(col-2)))
print("Creating INFO files", end="")
i = 0
for row in reader:

    infoname = "info" + str(i) + ".csv"
    info = open(infoname, "w", newline="")
    writer = csv.writer(info)

    writer.writerow(infos)

    for col in range(2, 2 + n_infos): #Starting from ETT column + 1
        if col == 2:
            writer.writerow(row[col])
        else:
            writer.writerow("," + row[col])
        
    info.close()
    i += 1

print("...done!\n")

