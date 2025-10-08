# https://open.kattis.com/contests/r3of2f/problems/vote
# https://vjudge.net/problem/Kattis-vote

def exercicio():
    n = int(input())

    votos = []

    maximo = 0
    contmaximo = 0

    for i in range(n):
        votos.append(int(input()))

        if(votos[i] == maximo):
            contmaximo += 1

        elif(votos[i] > maximo):
            maximo = votos[i]
            contmaximo = 1

    total = sum(votos)

    vencedor = max(votos)

    if(contmaximo > 1):
        return ("no winner")
    if((total / 2) < vencedor):
        return (f"majority winner {votos.index(vencedor) + 1}")
    
    return  (f"minority winner {votos.index(vencedor) + 1}")

T = int(input())

for k in range(T):
    print(exercicio())