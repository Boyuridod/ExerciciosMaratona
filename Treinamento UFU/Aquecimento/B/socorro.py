N = int(input())

while(N != 0):

    S = 0
    P = 0

    mat = []

    for i in range(N):
        mat.append(input().split(" "))

    mat = sorted(mat)

    i = 0
    incorreto = 0
    aux = mat[0][0]

    while(i < len(mat)):

        if(mat[i][2] == "incorreto"):
            incorreto += 1
        
        else:
            P += (incorreto * 20) + int(mat[i][1])
            S += 1
            aux = mat[i][0]
            incorreto = 0
            
        i += 1

    print(S,P)

    N = int(input())