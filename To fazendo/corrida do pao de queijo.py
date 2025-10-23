def calcula(t, cap):
    qtt = 0

    for i in cap:
        qtt += t * i

    return qtt

N = int(input())

paes = int(input())

cap = list(map(int, input().split(" ")))

tmax = paes * max(cap)

esq = 0
cent = tmax
dir = tmax 

menor = 1e10

while(True):
    if(calcula(cent, cap) > paes):
        dir = cent
    elif(calcula(cent, cap) < paes):
        esq = cent
    else:
        break

    cent = (esq + dir) // 2

print(cent)