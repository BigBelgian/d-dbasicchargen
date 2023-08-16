import operator
import random
class Character:
    def __init__(self,stats, job, level):
        self.stats = stats
        self.job = job
        self.level = level
        self.hitdice = "D4"
        self.health = 0
        if self.job == "Dwarf":
            self.hitdice = "D8"
        elif self.job == "Elf":
            self.hitdice = "D6"
        elif self.job == "Halfling":
            self.hitdice = "D6"
        elif self.job == "Fighter":
            self.hitdice = "D6"
        elif self.job == "Magic User":
            self.hitdice = "D4"
        elif self.job == "Thief":
            self.hitdice = "D4"
        elif self.job == "Cleric":
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
    if next(iter(sorted_stats)) == "str" and stats["con"] >= 9:
        return "Dwarf"
    elif (next(iter(sorted_stats)) == "str" and stats["int"] >= 9) or (next(iter(sorted_stats)) == "int" and stats["int"] >= 9):
        return "Elf"
    elif next(iter(sorted_stats)) == "str" and stats["dex"] >= 9 and stats["con"] >= 9 or next(iter(sorted_stats)) == "dex" and stats["dex"] >= 9 and stats["con"] >= 9:
        return "Halfling"
    elif next(iter(sorted_stats)) == "str" or sorted_stats["str"] > sorted_stats["dex"] and sorted_stats["str"] > sorted_stats["wis"] and sorted_stats["str"] > sorted_stats["int"]:
        return "Fighter"
    elif next(iter(sorted_stats)) == "int" or sorted_stats["int"] > sorted_stats["dex"] and sorted_stats["int"] > sorted_stats["wis"] and sorted_stats["int"] > sorted_stats["str"]:
        return "Magic User"
    elif next(iter(sorted_stats)) == "wis" or sorted_stats["wis"] > sorted_stats["dex"] and sorted_stats["wis"] > sorted_stats["str"] and sorted_stats["wis"] > sorted_stats["int"]:
        return "Cleric"
    elif next(iter(sorted_stats)) == "dex" or sorted_stats["dex"] > sorted_stats["str"] and sorted_stats["dex"] > sorted_stats["wis"] and sorted_stats["dex"] > sorted_stats["int"]:
        return "Thief"
    else:
        return "Fighter"
char = 1
while char >= 1:
    print ("welcome to the character creator for d&d basic. You can let the creator generate stats and recommend a class to play.")
    char = int(input("How many characters do you want to create? :"))
    opt = input("press Enter to create a character randomly, enter 1 to create a character with an array of stats :")
    party = {}
    if opt == "":
        lvl = input("enter Level:")
        stats = randomstats()
        person = Character(stats, classpicker(stats),int(lvl))
        party.pop(char, person)
        char -= 1
    elif opt =="1":
        stre = input("enter Strength:")
        dex = input("enter Dexterity:")
        con = input("enter Constitution:")
        smart = input("enter intelligence:")
        wis = input("enter Wisdom:")
        cha = input("enter Charisma:")
        stats = {"str" : int(stre) ,"dex" : int(dex) ,"con" : int(con) ,'int' : int(smart) ,"wis" : int(wis) ,"cha" : int(cha)}
        lvl = input("enter Level:")
        print(stats)
        person = Character(stats, classpicker(stats), int(lvl))
        party.pop(char, person)
        char -= 1
#for i in len(range(party.pop(char, person))):
person.charprint()
