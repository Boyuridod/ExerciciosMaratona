N = int(input())
participante = []

for i in range(N):
    participante.append(input().split(","))
    participante[i][1] = int(participante[i][1])

matriz_ordenada = sorted(participante, key=lambda x: x[0])
matriz_ordenada = sorted(matriz_ordenada, key=lambda x: x[1], reverse=True)

for linha in matriz_ordenada:
    print(linha[0])