N = int(input())

mercado = []

maior = 0

for i in range(N):
    mercado.append(input())

    if(len(mercado[i]) > maior):
        maior = len(mercado[i])

mercado.sort()

j = 0

for i in range(maior + 1):

    for j in mercado:

        if(len(j) == i):
            print(j)