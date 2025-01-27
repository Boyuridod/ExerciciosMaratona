N = int(input())

mat = [[0]*10]*10

certo = True

for i in range(N):
    D, L, R, C = input().split(" ")
    D = int(D)
    L = int(L)
    R = int(R) - 1
    C = int(C) - 1

    if(D == 0):
        j = C
        aux = C + L - 1
        while(j < aux - C):
            if(j < 10 and j >= 0):
                mat[R][j] += 1
                j += 1
            else:
                certo = False
                j = aux - C

    else:
        j = R
        aux = R + L - 1
        while(j < aux - R):
            if(j < 10 and j >= 0):
                mat[j][C] += 1
                j += 1
            else:
                certo = False
                j = aux - R

if(certo == True):
    for i in range(10):

        for j in range(10):

            if(mat[i][j] > 1):
                certo = False
                i = 9
                j = 9

        print(mat[i])

if(certo == True):
    print("Y")

else:
    print("N")