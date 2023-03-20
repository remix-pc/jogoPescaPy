from random import randrange
import os
import sys

nPlayers = 0
listPlayers = []
player = ''
nGames = 0
nFish = 0

try:
    nPlayers = int(input("Digite o número de jogadores: "))
    for i in range(nPlayers):
        player = input("Digite o nome do jogador: ")
        listPlayers.append(player)
    nGames = int(input("Digite o número de iscas: "))
    nFish = int(input("Quantos peixes? Digite o número: "))
except ValueError:
    print("Number please.")
    input("Aperte qualquer tecla e depois abra novamente o jogo.")
    sys.exit()
    



os.system('cls')

def table():
    for line in range(5):
        for column in range(10):
            print(f'  [{column},{line}]', end=" ")
        
    print("\n")


positions = None

fishTanks = list(range(nFish))




for i in range(nFish):
    positions = f'{randrange(10)} {randrange(6)}'
    alreadyHas = False
    for b in range(len(fishTanks)):
        if(positions == fishTanks[b]):
            alreadyHas = True
            break
    
    if(not alreadyHas):
        fishTanks[i] = positions
    else:
        i -= 1


#Game

points = list(range(nPlayers))

game = None


for i in range(nGames):
    table()
    roundGame = i
    print(f'RODADA: {roundGame + 1}')
    for x in range(nPlayers):
        print(f'{listPlayers[x]} é a sua vez! ')
        game = input("Insira a posição (x y) sem ponto ou virgula exemplo(3 5): ")

        for b in range(len(fishTanks) + 1):
            if(fishTanks[b] == game):
                print(f'{listPlayers[x]} ACERTOU, PARABÉNS!')
                points[x] = points[x] + 1
                fishTanks[b] = ""
                break
                

            if (b == (len(fishTanks) - 1)):
                print(f'{listPlayers[x]} sim, você errou.')
                break
    input("Aperte qualquer tecla para continuar")
    os.system('cls')
    

#Mostrando os pontos

for i in range(nPlayers):
    if points[i] == 0:
        print(f'{listPlayers[i]} você não pescou nada :/')
    else:
        print(f'{listPlayers[i]} pescou: {points[i]} peixes.')

#Result

highestScore = points[0]
winner = listPlayers[0]

for i in range(nPlayers):
    if(points[i] > highestScore):
        winner = listPlayers[i]
draw = 0
if(highestScore != 0):

    #Ver se deu empate

    for i in range(len(points)):
        if(points[i] == highestScore):
            draw += 1
    
    if(not (draw >= 2)):
        print(f'{winner} é o maior pescador de todos, meus parabéns!')
    else:
        print("Empate.")
else:
    print("Ninguém conseguiu pescar 1 peixe.")

print("\n")







    


