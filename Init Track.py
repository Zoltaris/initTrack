import random
import csv


playerNo = 0
enemyNo = 0
dieMin = 1
dieMax = 20
i = 0
n = 0
Players=[]
Enemies=[]
Participant=[]
newCombat = True
answered = False



class Entity:
    def __init__(self, name, initMod):
            self.name = name
            self.initMod = initMod
            self.initRol = 0
            self.initVal = 0


enemyNo=int(input("How many enemies?"))
Answered = False
with open('Player_List.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    cellCount = 0
    name = True
    playerDetails = []
    for row in csv_reader:
        if cellCount == 0:
            cellCount += 1
        else:
            print(row)
            p = Entity(row[0], row[1])
            Players.append(p)
            cellCount += 1    

while(n < enemyNo):
    nameEnter=input("What is the name of the enemy, with a description?")
    modEnter=int(input("What is their iniitiative Modifier?"))
    e = Entity(nameEnter, modEnter)
    Enemies.append(e)
    n=n+1

for enemy in Enemies:
    enemy.initRol = random.randrange(dieMin, dieMax)
    enemy.initVal = enemy.initRol + enemy.initMod
    Participant.append(enemy)


for player in Players:
    z = 'What did '+ player.name+ ' roll?'
    player.initRol = int(input(z))
    player.initVal = player.initRol + int(player.initMod)
    Participant.append(player)


Participant.sort(key=lambda participant: participant.initVal, reverse=True)
print("Name                 Initiative                      Modifier")
for person in Participant:
    print(person.name,"         ", person.initVal,"                  ", person.initMod)

k=input("press close to exit") 
