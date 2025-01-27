N = int(input())

C = []
qtt = []

for i in range(N):
    aux = int(input())

    if(aux in C):
        qtt[C.index(aux)] += 1

    else:
        C.append(aux)
        qtt.append(1)

aux = qtt

aux.sort(reverse=True)

aux = aux[0] #O maior nro de repeticoes

num = qtt.index(aux)

if(aux == 1):
    C.sort()

    print(C[-1], "1")

else:
    print(C[num], qtt[num])