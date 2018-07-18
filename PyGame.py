#Text-based fantasy adventure game
#Made to demonstrate basic python programming skills and knowledge

import random
import shelve

shelfFile = shelve.open('myToonData')
login = {}
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



shelfFile.close()
