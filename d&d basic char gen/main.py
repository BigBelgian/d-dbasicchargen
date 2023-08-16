import operator
import random
class Character:
    def __init__(self,stats, job, level):
        self.stats = stats
        self.job = job
        self.level = level
        self.hitdice = "D4"
        self.health = 0
        if self.job[0] == "Dwarf":
            self.hitdice = "D8"
        elif self.job[0] == "Elf":
            self.hitdice = "D6"
        elif self.job[0] == "Halfling":
            self.hitdice = "D6"
        elif self.job[0] == "Fighter":
            self.hitdice = "D6"
        elif self.job[0] == "Magic User":
            self.hitdice = "D4"
        elif self.job[0] == "Thief":
            self.hitdice = "D4"
        elif self.job[0] == "Cleric":
            self.hitdice = "D6"
        else:
            self.hitdice = "D4 (not set)"
        self.health = dr(self.level, int(self.hitdice[1]))

    def charprint(self):
        print("your stats are : " + str(self.stats))
        print("your class is : " + str(self.job))
        print("your level is : " + str(self.level))
        print("your hitdice are : " + str(self.hitdice))
        print("your health is : " + str(self.health))


def dr(ammount, dice, addition=0):
    result = 0
    while ammount > 0 :
        result = result + random.randint(1, dice)
        ammount -= 1
    result = result + addition
    return result
def randomstats():
    stats = {"str" : dr(3,6,0),"dex" : dr(3,6,0),"con" : dr(3,6,0),"int" : dr(3,6,0),"wis" : dr(3,6,0),"cha" : dr(3,6,0)}
    return stats
def classpicker(stats):
    sorted_stats = dict(sorted(stats.items(), key=operator.itemgetter(1), reverse=True))
    bestchar = []
    if next(iter(sorted_stats)) == "str" and stats["con"] >= 9:
            bestchar.append("Dwarf")
    if (next(iter(sorted_stats)) == "str" and stats["int"] >= 9) or (next(iter(sorted_stats)) == "int" and stats["int"] >= 9):
            bestchar.append("Elf")
    if next(iter(sorted_stats)) == "str" and stats["dex"] >= 9 and stats["con"] >= 9 or next(iter(sorted_stats)) == "dex" and stats["dex"] >= 9 and stats["con"] >= 9:
            bestchar.append("Halfling")
    if next(iter(sorted_stats)) == "str" or sorted_stats["str"] > sorted_stats["dex"] and sorted_stats["str"] > sorted_stats["wis"] and sorted_stats["str"] > sorted_stats["int"]:
            bestchar.append("Fighter")
    if next(iter(sorted_stats)) == "int" or sorted_stats["int"] > sorted_stats["dex"] and sorted_stats["int"] > sorted_stats["wis"] and sorted_stats["int"] > sorted_stats["str"]:
            bestchar.append("Magic User")
    if next(iter(sorted_stats)) == "wis" or sorted_stats["wis"] > sorted_stats["dex"] and sorted_stats["wis"] > sorted_stats["str"] and sorted_stats["wis"] > sorted_stats["int"]:
            bestchar.append("Cleric")
    if next(iter(sorted_stats)) == "dex" or sorted_stats["dex"] > sorted_stats["str"] and sorted_stats["dex"] > sorted_stats["wis"] and sorted_stats["dex"] > sorted_stats["int"]:
            bestchar.append("Thief")
    if len(bestchar) == 0:
        bestchar.append("Fighter")
    return bestchar
print ("welcome to the character creator for d&d basic. You can let the creator generate stats and recommend a class to play.")
charcount =1
char = int(input("How many characters do you want to create? :"))
lvl = input("enter Level for the party :")
opt = input("press Enter to create a character(s) randomly, enter 1 to create character(s) with an array of stats :")
party = []

while charcount <= char:
    print("Character " + str(charcount))
    statchange = "n"
    switch = ""
    tempstat = {}
    switch2 =""
    if opt == "":
        stats = randomstats()
        print(str(stats) + "\n Do you want to switch a stat?")
        statchange = input("y/n :")
        if statchange == "y":
            print ("which stats do you want to switch?")
            switch = input("(str - dex - con - int - wis - cha) :")
            tempstat =stats[switch]
            switch2 = input("(str - dex - con - int - wis - cha) :")
            stats[switch] = stats[switch2]
            stats[switch2] = tempstat
        person = Character(stats, classpicker(stats), int(lvl))
        party.append(person)
        charcount += 1
    elif opt =="1":
        stre = input("enter Strength:")
        dex = input("enter Dexterity:")
        con = input("enter Constitution:")
        smart = input("enter intelligence:")
        wis = input("enter Wisdom:")
        cha = input("enter Charisma:")
        stats = {"str" : int(stre) ,"dex" : int(dex) ,"con" : int(con) ,'int' : int(smart) ,"wis" : int(wis) ,"cha" : int(cha)}
        person = Character(stats, classpicker(stats), int(lvl))
        party.append(person)
        charcount += 1
for i in range(len(party)):
    print("character " + str(i+1))
    party[i].charprint()

#person.charprint()
