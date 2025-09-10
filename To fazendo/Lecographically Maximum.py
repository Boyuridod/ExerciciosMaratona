# https://vjudge.net/contest/747064#problem/L

# TLE

N = int(input())
a = list(map(int, input().split(" ")))

a.sort(reverse=True)

for i in range(len(a)):
    a[i] = list(map(int, format(a[i], "b")))

for i in a:
    for j in range(len(a[0]) - len(i)):
        i.insert(0, 0)

for i in range(len(a[0])):
    qtt = 0
    for j in range(len(a)):
        if(a[j][i] == 1):
            qtt += 1
    for j in range(len(a)):
        if(qtt > 0):
            a[j][i] = 1
            qtt -= 1
        else:
            a[j][i] = 0

for i in a:
    aux = "".join(map(str, i))
    aux = int(aux, 2)

    print(aux, end=" ")

print("")