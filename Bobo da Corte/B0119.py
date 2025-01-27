N = int(input())

carlos = int(input())

ganhou = True

for i in range(N - 1):
    atual = int(input())

    if(atual > carlos):
        ganhou = False

if(ganhou == True):
    print("S")

else:
    print("N")