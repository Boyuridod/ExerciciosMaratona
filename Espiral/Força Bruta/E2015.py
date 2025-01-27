def printamatriz(matri, A):
    for i in matri:
        print(i)

    print(A,"\n")

N, B = input().split()
N = int(N)
B = int(B)

matriz = [[0]*N]

for i in range(N - 1):
    matriz.append(matriz[0].copy())

x = 0
y = 0

parada_x = 0
parada_y = 0

while(B > 0):

    while(x < N and B > 0):
        matriz[y][x] = 1
        x += 1
        B -= 1
        # printamatriz(matriz, B)

    y += 1

    x -= 1

    while(y < N and B > 0):
        matriz[y][x] = 1
        y += 1
        B -= 1
        # printamatriz(matriz, B)

    N -= 1

    y -= 1

    x -= 1

    while(x > parada_x and B > 0):
        matriz[y][x] = 1
        x -= 1
        B -= 1
        # printamatriz(matriz, B)

    parada_x += 1

    parada_y += 1

    while(y > parada_y and B > 0):
        matriz[y][x] = 1
        y -= 1
        B -= 1
        # printamatriz(matriz, B)

print(y + 1, x + 2)