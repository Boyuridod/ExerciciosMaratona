N = int(input())

lista = []
votos_cafes = [[]]

for i in range(N):
    lista.append(input())

lista.sort()

for i in lista:
    if(i not in votos_cafes[0]):
        votos_cafes[0].append(i)
        votos_cafes[1].append(1)
    else:
        votos_cafes[1][votos_cafes[0].index(i)] += 1

print(votos_cafes)