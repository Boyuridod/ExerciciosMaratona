C = int(input())
maior = saldo = 100

for i in range(C):
    saldo += int(input())

    if(saldo > maior):
        maior = saldo
    
print(maior)