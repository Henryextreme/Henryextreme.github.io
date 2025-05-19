import random
from itertools import count

largura = 5
altura = 5
numBomba = 9
qtBandeiras = 0
qtBombas = 2
tabuleiro = []
tabStatus = []
tabBandeiras = []
valorPadrao = 0

def CriaTabuleiro(tabuleiro, altura, largura, valorPadrao):
    for x in range (0, largura):
        linha = []
        for y in range (0,altura):
            linha.append(valorPadrao)
        tabuleiro.append(linha)

def MostraTabuleiro(tabuleiro):
    for x in range (0, len(tabuleiro)):
        print(tabuleiro[x])


###
###popula o tabuleiro
###
def CriarBombas(tabuleiro,qtBombas,numBomba):
    cont = 0
    for x in range (0,qtBombas):
        posX = random.randint(0,largura -1)
        posY= random.randint(0, altura -1)

        while tabuleiro[posX][posY] == numBomba:
            posX = random.randint(0, largura - 1)
            posY = random.randint(0, altura - 1)
            cont += 1
        if tabuleiro[posX][posY] != numBomba:
            tabuleiro[posX][posY] = numBomba


def ContaBombas (tabuleiro,numBomba):
    for y in range(0,len(tabuleiro)):
        for x in range (0,len(tabuleiro[y])):
            if tabuleiro[x][y] != numBomba:
                cont = 0
                ##check vertical
                if y > 0 :
                    if tabuleiro[y-1][x] == numBomba: cont +=1
                if y < altura-1:
                    if tabuleiro[y+1][x] == numBomba: cont +=1

                ##check horizontal
                if x < largura-1:
                    if tabuleiro[y][x+1] == numBomba: cont +=1
                if x > 0 :
                    if tabuleiro[y][x-1] == numBomba: cont +=1
                tabuleiro [y][x] = cont

                ##check diagonal superior
                if x < 0 and y > 0:
                    if tabuleiro[y+1][x-1] == numBomba: cont +=1
                if x > largura and y > 0:
                    if tabuleiro[y+1][x+1] == numBomba: cont +=1
                tabuleiro [y][x] = cont

                ##check diagonal inferior
                if x < 0 and y < 0:
                    if tabuleiro[y-1][x-1] == numBomba: cont +=1
                if x > largura and y < 0:
                    if tabuleiro[y-1][x+1] == numBomba: cont +=1
                tabuleiro [y][x] = cont





CriaTabuleiro(tabuleiro,altura,largura, valorPadrao)
CriarBombas(tabuleiro,qtBombas,numBomba)
ContaBombas(tabuleiro,numBomba)
MostraTabuleiro(tabuleiro)


