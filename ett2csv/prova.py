import sys
import os
import zipfile
import csv

from lib import *

f = open("team.txt", "r")
flist = f.readlines()
#print(flist)

db = open("db.cvs", "w")
writer = csv.writer(db)

def read_pkm(pkm):
    PKM = {"specie":"", "obj":"", "ability":"", "HP":0, "Atk":0, "Def":0, "SpA":0, "SpD":0, "Spe":0, "nature":"", "iv_HP":31, "iv_Atk":31, "iv_Def":31, "iv_SpA":31, "iv_SpD":31, "iv_Spe":31}
    stats = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]
    move_counter = 0
    for line in pkm:
        #Read specie and object
        if "@" in line:
            at = line.index("@")
            PKM["specie"] = line[0:at-1]
            #print(PKM["specie"])
            PKM["obj"] = line[at+2:-2]
            #print(PKM["obj"])
            #print(len(PKM["obj"]))

        #Read ability
        elif "Ability" in line:
            col = line.index(":")
            PKM["ability"] = line[col+2:-3]
            #print(PKM["ability"])
        
        #Read EV spread
        elif "EVs" in line:
            for stat in stats:
                stat_index = line.find(stat)
                #print(stat_index)
                if stat_index != -1:
                    PKM[stat] = line[stat_index-4:stat_index-1]
                    PKM[stat] = PKM[stat].replace("/", "")
                    PKM[stat] = PKM[stat].replace(" ", "")
                    PKM[stat] = PKM[stat].replace(":", "")
                #print(PKM[stat])
        
        #Read Nature
        elif "Nature" in line:
            nature_index = line.find("Nature")
            PKM["nature"] = line[0:nature_index-1]
            #print(PKM["nature"])

        #Read IVs
        elif "IVs" in line:
            for stat in stats:
                iv_index = line.find(stat)
                iv_stat = "iv_" + stat
                #print(iv_index)
                if iv_index != -1:
                    PKM[iv_stat] = line[iv_index-4:iv_index-1]
                    PKM[iv_stat] = PKM[iv_stat].replace("/", "")
                    PKM[iv_stat] = PKM[iv_stat].replace(" ", "")
                    PKM[iv_stat] = PKM[iv_stat].replace(":", "")
                #print(PKM[iv_stat])
        
        #Read moves
        elif "-" in line:
            move_counter += 1
            move_n = "move" + str(move_counter)
            PKM[move_n] = line[2::]
            PKM[move_n] = PKM[move_n].replace("\n", "")
            PKM[move_n] = PKM[move_n].replace("  ", "")
            #print(PKM[move_n])

    #print(PKM)
    return PKM

#Separate Pokemon in the same team
low_index = 0
for el in range(6):
    high_index = flist.index("\n", low_index+1)
    #print(high_index)
    pkm = flist[low_index:high_index]

    PKM = read_pkm(pkm)
    #print(PKM)
    if el == 0:
        writer.writerow(PKM.keys())
    writer.writerow(PKM.values())

    low_index = high_index

db.close()
f.close()


'''
to do:
- add teammates
- add competition score
- generalize to many team.txt file in a zip archive
'''

