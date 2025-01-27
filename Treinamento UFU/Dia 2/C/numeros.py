N = int(input())

lista = list(input().split(" "))

impar = []
par = []

for i in range(N):
    x = int(lista[i])
    if(x % 2 == 0):
        par.append(x)
    else:
        impar.append(x)

impar.sort()
par.sort()

for i in impar:
    print(i, end=" ")

for i in par:
    print(i, end=" ")