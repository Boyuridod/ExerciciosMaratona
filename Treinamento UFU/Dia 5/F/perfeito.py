N = int(input())

teste = []
resul = []

for i in range(1,N):
    if(N % i == 0):
        teste.append(i)

    if(sum(teste) == i):
        resul.append(i)

if(sum(teste) == N):
    print("sim")
else:
    print("nao")