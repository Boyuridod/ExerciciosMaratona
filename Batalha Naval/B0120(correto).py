import numpy as np

N = int(input())

#mat = np.zeros(shape=(10,10), dtype=int)

mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

certo = True

for i in range(N):
    D, L, R, C = input().split(" ")
    D = int(D)
    L = int(L)
    R = int(R) - 1
    C = int(C) - 1

    if(D == 0):
        if(C + L > 9 or C + L < 0):
            certo = False
            break

        else:
            for y in range(C,C+L):

                if(mat[R][y] == 1):
                    certo = False
                    break
                else:
                    mat[R][y] = 1

    else:
        if(R + L > 9 or R + L < 0):
            certo = False
            break

        else:
            for x in range(R,R+L):

                if(mat[x][C] == 1):
                    certo = False
                    break
                else:
                    mat[x][C] = 1

    if(not certo):
        break


if(certo):
    print("Y")

else:
    while(i < N - 1):
        D, L, R, C = input().split(" ")

        i += 1

    print("N")