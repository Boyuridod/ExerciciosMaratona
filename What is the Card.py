# https://vjudge.net/problem/UVA-10646

values = {
    'A': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'T': 10
}

def exercicio(i):
    y = 0

    decks = list(input().split(" "))

    decks.reverse()

    mao = decks[0: 25]

    pilha = decks[25: len(decks)]

    for j in range(3):

        if(len(pilha) > 0):
            try:
                x = values[pilha[0][0]]
            except:
                x = int(pilha[0][0])

            y += x

            try:
                for k in range((10 - x) + 1):
                    pilha.pop(0)
            except:
                continue


    pilha = mao + pilha

    pilha.reverse()

    print(f"Case {i + 1}: {pilha[y - 1]}")

n = int(input())

for i in range(n):
    exercicio(i)