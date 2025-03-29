def Fatorial(nro):
    if (nro==1):
        return 1
    return nro * Fatorial(nro-1)

def Fatorial2(nro):
    fat=1
    for i in range(1,nro+1):
        fat *= i
    return fat

valor = int(input("informe um valor: "))
print(f"O fatorial de {valor} é {Fatorial2(valor)}")