N = int(input())

for i in range(N):
    X = int(input())
    matriz = []
    for j in range(X):
        matriz.append(input().split(" "))
        matriz[j] = [int(elemento) for elemento in matriz[j]]

    x = y = sucesso = cont = 0

    while(cont <= 8 and sucesso == 0):
        while(matriz[y][x + 1] != 1 and x > X - 1):
            x += 1
        while(matriz[y + 1][x] != 1 and y > X - 1):
            y += 1
        while(matriz[y][x + 1] != 1 and x > X - 1):
            x += 1
        if(matriz[y + 1][x] != 1 and y > X - 1):
            while(matriz[y + 1][x] != 1 and y > X - 1):
                y += 1
        else:
            while

        cont += 1

        if(x == y == X):
            sucesso = 1

    print(sucesso)