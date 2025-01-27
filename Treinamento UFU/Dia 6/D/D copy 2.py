import numpy as np
N = int(input())

qttDino = []
maximo = 0
for i in range(N):
    D, A = map(int, input().split(" "))
    
    aux = np.linspace(D,A,(A-D)+1)

    for i in aux:
        qttDino.append(i)

for i in range(len(qttDino)):
    if maximo < qttDino.count(i):
        maximo = qttDino.count(i)

print(maximo)