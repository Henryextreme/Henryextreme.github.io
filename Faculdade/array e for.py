def fatorial(nro):
    if (nro==1):
        return 1
    return nro*fatorial(nro-1)

print(fatorial(5))