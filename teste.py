largura = 5
altura = 5
numBomba = 9
qtBandeiras = 0
qtBombas = 5
tabuleiro = []
tabStatus = []
larg = []
tabBandeiras = []
valorPadrao = 0

def CriaTabuleiro(tabuleiro, altura, largura, valorPadrao):
    for x in range (0, largura):
        linha = []
        for y in range (0,altura):
            linha.append(valorPadrao)
        tabuleiro.append(linha)

def MostraTabuleiro(tabuleiro,largura,larg):
    for y in range(0,largura):
        larg.append(y)
    print(" ",larg)
    for x in range (0, len(tabuleiro)):
        print(x,tabuleiro[x])
    


CriaTabuleiro(tabuleiro,altura,largura, valorPadrao)
MostraTabuleiro(tabuleiro,largura,larg)

