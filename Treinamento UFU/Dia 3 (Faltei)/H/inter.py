N = int(input())

for i in range(N):
    lista = input().split(" ")

    for j in range(len(lista)):
        lista[j] = float(lista[j])

    print(lista[0] > lista[1] and lista[0] < lista[2])