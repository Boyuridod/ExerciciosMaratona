#USAR AS VARIAVEIS X E Y PARA SIMULAR O LOCAL QUE ESTOU NA MATRIZ!!!
#Link não disponivel

N, B = map(int, input().split(" "))

x = y = 0

parax = [1, N]
paray = [1, N]

while(B > 0):

    if(B > (parax[1] - parax[0])):
        B -= parax[1] - parax[0] + 1
        x += parax[1]

    else:
        x += B
        break

    if(B > (paray[1] - paray[0])):
        B -= paray[1] - paray[0] + 1
        y += paray[1]

    else:
        y -= B
        break

    #erro

    if(B > (parax[1] - parax[0])):
        B -= parax[1] - parax[0] + 1
        x -= parax[0]

    else:
        x += B

    if(B > (parax[1] - parax[0])):
        B -= parax[1] - parax[0] + 1
        x -= parax[0]

    else:
        y -= B