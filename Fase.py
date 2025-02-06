N = int(input())
K = int(input())

lista = []

for i in range(N):
    lista.append(int(input()))

lista.sort(reverse=True)

cont = K

if(K != N):

    for i in range(K, len(lista) - 1):
        if(lista[K - 1] == lista[i]):
            cont += 1

        else:
            break

    if(lista[cont - 1] == lista[cont]):
        cont += 1

    print(cont)

else:
    print(K)