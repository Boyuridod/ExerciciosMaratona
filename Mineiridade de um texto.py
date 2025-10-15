# https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/H

n = int(input())

dicionario = {}

for i in range(n):
    palavra, pontuacao = list(input().split(" "))

    dicionario[palavra] = int(pontuacao)

frase = input()

frase = frase[0: len(frase) -2].split(" ")

mineiridade = 0

for i in frase:
    try:
        mineiridade += dicionario[i]
    except:
        mineiridade += 0

print(mineiridade)