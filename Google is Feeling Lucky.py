# https://vjudge.net/problem/UVA-12015

def exercicio(n):
    sites = {}
    maior = 0
    for i in range(10):
        site, nota = input().split(" ")
        nota = int(nota)
        sites[site] = nota

        if(nota > maior):
            maior = nota

    print(f"Case #{n}:")
    for i in sites:
        if(sites[i] == maior):
            print(i)

N = int(input())

for i in range(1, N + 1, 1):
    exercicio(i)