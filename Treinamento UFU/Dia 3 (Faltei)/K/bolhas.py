Q = int(input())

cont = 0

for i in range(Q):
    S = int(input())

    if(S >= 4):
        cont += S - 3

print(cont)