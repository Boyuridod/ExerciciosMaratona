N = int(input())

lista = []

for i in range(N):
    lista.append(input())

lista.sort()

for i in lista:
    print(i)