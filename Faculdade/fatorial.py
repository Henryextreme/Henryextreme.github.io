print("Digite um numero para fazer a fatorial")
numero = int(input())
fato = 1
for X in range (1,1+numero):
    fato = fato * X

print("a fatorial de",numero,"é igual a",fato)