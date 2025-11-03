# https://neps.academy/br/exercise/248

N = int(input())
consultas = []
cont = 1

for i in range(N):
    consultas.append(list(map(int, input().split(" "))))

while(cont < N):
    if(consultas[cont][0] < consultas[cont - 1][1]):
        consultas.pop(cont)
        N -= 1
    
    cont += 1

print(len(consultas))