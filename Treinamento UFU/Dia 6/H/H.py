def busca(L, palavra):
    verifica = 0
    i = 0
    j = 0
    while i != 10 and verifica == 0: 
        j = 0
        while j != 10  and verifica == 0:
            if L[i][j] == palavra[0]:
                verifica = procura(L, palavra, i, j)
            j+=1
        i+=1
    print(verifica)

def procura(L, palavra, a, b):
    verifica = 0
    for i in range(len(palavra)):
        if b+i < 10 and L[a][b+i] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if b-i >= 0 and L[a][b-i] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if a+i < 10 and L[a+i][b] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if b-i >= 0 and L[a-i][b] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if a+i < 10 and b+i < 10 and L[a+i][b+i] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if a+i < 10 and b-i >= 0 and L[a+i][b-i] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if a-i >= 0 and b+i < 10 and L[a-i][b+i] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    verifica = 0
    for i in range(len(palavra)):
        if a-i >= 0 and b-i >= 0 and L[a-i][b-i] == palavra[i]:
            verifica += 1
    if verifica == len(palavra):
        return 1
    return 0
        

L = []

for i in range(10):
    L.append(input().split(" "))

for i in range(8):
    palavra = input()
    busca(L, palavra)