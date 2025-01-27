N = int(input())

ganhou = 0

for i in range(N):
    porta = int(input())

    if(porta != 1):
        ganhou += 1

print(ganhou)