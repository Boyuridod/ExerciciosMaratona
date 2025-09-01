# https://vjudge.net/contest/744581#problem/C

def exercicio():
    jogadores = int(input(""))

    ganhador = list(map(int, input().split(" ")))

    if(jogadores == 2):
        if(ganhador[0] == ganhador[1]):
            return "YES"
        else:
            return "NO"
        
    else:
        if(ganhador[0] == 1 and ganhador[1] == 1 and ganhador[2] == 1):
            return "YES"
        
        if(ganhador[-1] == 0 and ganhador[-2] == 0):
            return "YES"
        
        for i in range(1, len(ganhador) - 1, 1):
            if(ganhador[i] == ganhador[i + 1] == 0):
                return "YES"
            if(ganhador[i - 1] == ganhador[i] == ganhador[i + 1] == 0):
                return "YES"
            if(ganhador[i - 1] == 0 and ganhador[i] == 0 and ganhador[i + 1] == 1):
                return "YES"
            if(ganhador[i - 1] == 1 and ganhador[i] == 0 and ganhador[i + 1] == 0):
                return "YES"
            
            # print(ganhador[i - 1], ganhador[i], ganhador[i + 1])
            # print(ganhador[i - 1] == 0 and ganhador[i] == 0 and ganhador[i + 1] == 1)
            
    return "NO"

n = int(input())

for asasas in range(n):
    print(exercicio())