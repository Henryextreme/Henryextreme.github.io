import random
from itertools import count

largura = 10
altura = 10
numBomba = 9
qtBandeiras = 0
qtBombas = 20
tabuleiro = []
tabStatus = []
larg = []
tabBandeiras = []
valorPadrao = 0

def CriaTabuleiro(tabuleiro, altura, largura, valorPadrao):
    for x in range (0,largura):
        linha = []
        for y in range (0,altura):
            linha.append(valorPadrao)
        tabuleiro.append(linha)

def MostraTabuleiro(tabuleiro,largura,larg):
    for y in range(0,largura):
        larg.append(y)
    print("  ",', '.join(map(str, larg)))
    for x in range (0, len(tabuleiro)):
        print(x,tabuleiro[x])


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
                    if tabuleiro[x][y-1] == numBomba: cont +=1
                if y < altura-1:
                    if tabuleiro[x][y+1] == numBomba: cont +=1

                ##check horizontal
                if x < largura-1:
                    if tabuleiro[x+1][y] == numBomba: cont +=1
                if x > 0 :
                    if tabuleiro[x-1][y] == numBomba: cont +=1
                
                ##check diagonal superior
                ##esquerda superior
                if y > 0 and x > 0: 
                    if tabuleiro[x-1][y-1] == numBomba: cont +=1
                ##direita superior
                if y > 0 and x < largura-1:
                    if tabuleiro[x+1][y-1] == numBomba: cont +=1
                
                ##check diagonal inferior
                ##esquerda inferior
                if y < altura - 1 and x > 0:
                    if tabuleiro[x-1][y+1] == numBomba: cont +=1
                ##direita inferior
                if y < altura - 1 and x < largura - 1:
                    if tabuleiro[x+1][y+1] == numBomba: cont +=1

                tabuleiro [x][y] = cont


#teste


CriaTabuleiro(tabuleiro,altura,largura, valorPadrao)
CriarBombas(tabuleiro,qtBombas,numBomba)
ContaBombas(tabuleiro,numBomba)
MostraTabuleiro(tabuleiro,largura,larg)


