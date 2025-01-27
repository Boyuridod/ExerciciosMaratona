N, M = input().split(" ")
N = int(N) #Interruptores
M = int(M) #Lampadas

lampadas = [0] * M

acesas = list(input().split(" "))

for i in range(1, int(acesas[0]) + 1):
    lampadas[int(acesas[i]) - 1] = 1

interruptores = []

for i in range(N):
    aux = list(input().split(" "))
    
    interruptores.append(aux)

inicial = lampadas.copy()

x = 0
cont = 1
certo = True

while(certo):
    for i in range(1,int(interruptores[x][0]) + 1):
        if(lampadas[int(interruptores[x][i]) - 1] == 1):
            lampadas[int(interruptores[x][i]) - 1] = 0

        else:
            lampadas[int(interruptores[x][i]) - 1] = 1

    if(lampadas == inicial and cont > M):
        certo = False

    if(lampadas == [0]*M):
        break

    if(x == N - 1):
        x = 0
    else:
        x += 1

    cont += 1

if(int(acesas[0]) == 0):
    print("0")
    
elif(certo):
    print(cont)

else:
    print("-1")