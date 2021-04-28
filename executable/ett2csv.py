import sys
import os
import zipfile
import csv

#from lib import *

######################################################################
#READ PKM function

def read_pkm(pkm):
    #Create a filtered (from "\n") list 
    pkm = [x for x in pkm if x != "\n"]
    print(pkm)

    PKM = {"specie":"", "obj":"", "ability":"", "HP":0, "Atk":0, "Def":0, "SpA":0, "SpD":0, "Spe":0, "nature":"", "iv_HP":31, "iv_Atk":31, "iv_Def":31, "iv_SpA":31, "iv_SpD":31, "iv_Spe":31}
    stats = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]
    move_counter = 0
    for line in pkm:
        #Read specie and object
        if line == pkm[0]:
            print(line)
            if "@" in line:
                at = line.index("@")
                PKM["specie"] = get_specie(line[0:at-1])
                #print(PKM["specie"])
                PKM["obj"] = line[at+2:-2]
                #print(PKM["obj"])
                #print(len(PKM["obj"]))
            else:
                PKM["specie"] = get_specie(line)

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
#######################################################################
#READ TEAM function

def read_team(flist, j):
    low_index = 0
    specie = []
    TEAM = []
    for el in range(6):
        if el != 5: #last party member has not the \n in the very end
            high_index = flist.index("\n", low_index+1)
        else:
            high_index = len(flist)
        #print(high_index)
        
        pkm = flist[low_index:high_index]
        #print(pkm)

        PKM = read_pkm(pkm)
        TEAM.append(PKM)

        specie.append(PKM["specie"])

        low_index = high_index
    
    return TEAM, specie

##################################################################
#ADD TEAMMATES

def add_teammates(TEAM, species):
    for PKM in TEAM:
        i = 1
        for specie in species:
            if PKM["specie"] != specie:
                tm_key = "teammate" + str(i)
                PKM[tm_key] = specie
                i += 1
    
    return TEAM

##################################################################
#PKM NICKNAMES

#pre_at is the substring of the first pkm line before the symbol @
def get_specie(pre_at):
    #Unfortunately SD put some info in () even if there is no nickname
    exceptions = ["M", "F", "Gigamax", "Galar", "Alola"]
    if "(" in pre_at and ")" in pre_at:
        left = pre_at.index("(")
        right = pre_at.index(")")
        if pre_at[left+1:right] not in exceptions:
            specie = pre_at[left+1:right]
        else:
            specie = pre_at
    else:
        specie = pre_at
    
    return specie

##################################################################
#MAIN

db = open("db.csv", "w", newline="")
writer = csv.writer(db)

archive = zipfile.ZipFile("teams.zip", "r")
print("N. of teams: " + str(len(archive.namelist())))
archive.extractall()

j = 0
for team in archive.namelist():
    print("Converting " + str(team))
    f = open(team, "r")
    flist = f.readlines()
    #print(flist)

    TEAM, species = read_team(flist, j)
    #print(TEAM)
    TEAM_wt = add_teammates(TEAM, species)

    if j==0:
        writer.writerow(TEAM_wt[0].keys())
    for PKM in TEAM_wt:
        writer.writerow(PKM.values())
        
    j += 1

    f.close()
    os.remove(team)

db.close()







'''
to do:
- add teammates (done)
- add competition score
- generalize to many team.txt file in a zip archive
'''

