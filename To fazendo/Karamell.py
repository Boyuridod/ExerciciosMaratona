# https://vjudge.net/contest/747064#problem/K

def printAlternado(x, y):
    bo = 0
    al = 0

    tot = len(x+y)

    y.sort()

    for i in range(tot):
        if(i % 2 == 0 and bo < len(y)):
            print(y[bo], end=" ")
            bo += 1
        else:
            print(x[al], end=" ")
            al += 1

    print(" ")

N = int(input())

a = list(map(int, input().split(" ")))

al = []
bo = []

if(sum(a) % 2 != 0):
    print(-1)

else:
    a.sort(reverse=True)

    for i in a:
        if(sum(al) <= sum(bo)):
            al.append(i)
        else:
            bo.append(i)

    if(sum(al) != sum(bo)):
        print(sum(al), sum(bo))
        print(-1)

    else:
        if(len(al) >= len(bo)):
            printAlternado(al, bo)
        else:
            printAlternado(bo, al)