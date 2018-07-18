import shelve
shelfFile = shelve.open('myToonData')

login = []

hp = 100
atk = 5
defend = 0
spd = 1
CharLvl = 1
CharExp = 0
name = 'Adam'

Adam = { 'myName': name, 'CharLvl': CharLvl, 'hp': hp, 'atk': atk,
                    'defend': defend, 'spd': spd, 'CharExp': CharExp }

login = [Adam]

print(login)

login.insert(0, input())



print(len(login))

login[toonData] = shelfFile['login[toonData]']

print(len(login)

shelfFile.close()
