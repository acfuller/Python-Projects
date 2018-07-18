#Text-based fantasy adventure game
#Made to demonstrate basic python programming skills and knowledge

import random
import shelve

shelfFile = shelve.open('myToonData')
login = {}
shelfFile['saveFile'] = login
#if login in shelfFile['myToonData'] == False:
#    shelfFile['saveFile'] = login
#elif login in shelfFile['myToonData'] == True:
#    login = shelfFile['login[saveFile]']
login = shelfFile['login[saveFile]']


while True:
    print("Are we starting a new Game(type ng) or Continueing(type c)?")
    new_game = input()

    if new_game.lower() == 'ng':
        print("What should I save your game under?")
        saveFile = input()
        print("Hello adventurer, what is your name?")
        name = input()
        hp = 100
        atk = 5
        defend = 0
        spd = 1
        CharLvl = 1
        CharExp = 0

        login[saveFile] = {'name': name, 'CharLvl': CharLvl, 'hp': hp, 'atk': atk,
                    'defend': defend, 'spd': spd, 'CharExp': CharExp }


        print("\nIt is wonderful to see you!" +
                "\nYou came at the right time," +
                " for we have a huge problem! \nMonsters from the " +
                "countryside are " +
                "attacking! \n" + "Please help us!")

        shelfFile['login[saveFile]'] = login
        break

    elif new_game.lower() == 'c':
        print("Welcome back adventurer! What is your save file?")
        saveFile = input()
        if saveFile not in login:
            print("No such user! Please try again!\n")
            continue
        else:
            print("Welcome back " + login[saveFile]['name'] + "!")
        break

    else:
        print("That doesn't make any sense! Try again!")
        continue

print(" ")


def lvlup():
    login[saveFile]['hp'] = login[saveFile]['hp'] + random.randint(1, 10)
    login[saveFile]['atk'] = login[saveFile]['atk'] + random.randint(0, 3)
    login[saveFile]['defend'] = login[saveFile]['defend'] + random.randint(0, 3)
    login[saveFile]['spd'] = login[saveFile]['spd'] + random.randint(0, 3)
    login[saveFile]['CharLvl'] = login[saveFile]['CharLvl'] + 1
    print("You have grown stronger! You are now level " +
    str(login[saveFile]['CharLvl']) + "!" + " Health: " +
    str(login[saveFile]['hp']) + " Attack: " + str(login[saveFile]['atk']) +
    " Defense: " + str(login[saveFile]['defend']) + " Speed: " +
    str(login[saveFile]['spd']) + "!")
    shelfFile['login[saveFile]'] = login

class enemy:

    def __init__(self, name, hp, atk, defend, spd, exp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defend = defend
        self.spd = spd
        self.exp = exp

goblin = enemy('goblin', 75, 3, 0, 2, 10)
orc = enemy('orc',105, 6, 3, 1, 20)
bandit = enemy('bandit', 100, 4, 0, 1, 15)
bear = enemy('bear', 200, 10, 5, 2, 30)
dragon = enemy('dragon', 1000, 100, 50, 25, 50)
magical_shrine = enemy('magical shrine', 0, 0, 0, 0, 20)


enemyList = [goblin, orc, bandit, bear, dragon, magical_shrine]

def encounter():
    global login
    global enemyList
    currentEnemy = enemyList[random.randint(0, 5)]
    print("You have encountered a " + currentEnemy.name + "!")
    while True:
        if currentEnemy.name == 'dragon':
            print("A mighty dragon has appeared and destroyed everything! \n"
            + "The entire kingdom is now in ruins. \n"
            + "You have died.")
            break
        elif currentEnemy.name == 'magical shrine':
            print("You have encountered a magical shrine!")
            login[saveFile]['CharExp'] = login[saveFile]['CharExp'] + 20
            if login[saveFile]['CharExp'] >= 50:
                lvlup()
                login[saveFile]['CharExp'] = login[saveFile]['CharExp'] % 50
            shelfFile['login[saveFile]'] = login
            break
        elif currentEnemy.hp <= 0:
            print("You have defeated the " + currentEnemy.name + '!')
            login = shelfFile['login[saveFile]']
            login[saveFile]['CharExp'] = login[saveFile]['CharExp'] + currentEnemy.exp
            if login[saveFile]['CharExp'] >= 50:
                lvlup()
                login[saveFile]['CharExp'] = login[saveFile]['CharExp'] % 50
            shelfFile['login[saveFile]'] = login
            break
        elif login[saveFile]['hp'] <= 0:
            print("You have died!")
            login = shelfFile['login[saveFile]']
            break
        else:
            currentEnemy.hp = currentEnemy.hp - (login[saveFile]['atk'] * login[saveFile]['spd'])
            login[saveFile]['hp'] = login[saveFile]['hp'] - (currentEnemy.atk * currentEnemy.spd)
            continue

while True:
    print("Would you like to go into the wild?\n(Yes/No)")
    toonAction = input()
    if toonAction.lower() == 'yes':
        encounter()
    else:
        print("Have a good rest and come back soon!"
        + "\nWe can spare much time!")
        login = shelfFile['login[saveFile]']
        quit()



shelfFile.close()
