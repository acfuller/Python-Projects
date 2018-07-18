import random
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

enemyList = [goblin, orc, bandit, bear, dragon]
login = {}
name = 'Adam'
hp = 100
atk = 5
defend = 0
spd = 1
CharLvl = 1
CharExp = 0
saveFile = "Adam"
login[name] = {'name': name, 'CharLvl': CharLvl, 'hp': hp, 'atk': atk,
            'defend': defend, 'spd': spd, 'CharExp': CharExp }


def encounter():
    currentEnemy = enemyList[random.randint(0, 4)]
    print("You have encountered a " + currentEnemy.name + "!")
    while true:
        if random.randint(0, 10) >= 9:
            print("You have encountered a magical shrine!")
            login[name]['CharExp'] = login[name]['CharExp'] + 45
            if login[name]['CharExp'] >= 50:
                lvlup()
                login[name]['CharExp'] = login[name]['CharExp'] % 50
        elif currentEnemy.hp <= 0:
            print("You have defeated the " + currentEnemy + '!')
            login = shelfFile['login[saveFile]']
            login[name]['CharExp'] = login[name]['CharExp'] + currentEnemy.exp
            if login[name]['CharExp'] >= 50:
                lvlup()
                login[name]['CharExp'] = login[name]['CharExp'] % 50
            break
        elif login[name]['hp'] <= 0:
            print("You have died!")
            login = shelfFile['login[saveFile]']
            break
        else:
            currentEnemy.hp = currentEnemy.hp - (login[name]['atk'] * login[name]['spd'])
            login[name]['hp'] = login[name]['hp'] - (currentEnemy.atk * currentEnemy.spd)
            continue


encounter()
#print(login[name]['hp'])
#print(enemyList[random.randint(0, 4)].hp)
