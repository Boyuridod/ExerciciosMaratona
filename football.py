# https://codeforces.com/problemset/problem/96/A

jogadores = input()

cont = 0
maior = 0
contZero = 0
maiorZero = 0

for i in jogadores:
    if i == '1':
        cont += 1
        if(contZero > maiorZero):
            maiorZero = contZero
    else:
        if(cont > maior):
            maior = cont
        cont = 0
        contZero += 1

if(maior > 7 or maiorZero > 7):
    print("YES")
else:
    print("NO")