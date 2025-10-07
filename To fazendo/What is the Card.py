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

    mao = decks[0: 25]

    pilha = decks[25: len(decks)]

    for j in range(3):

        if(len(pilha) > 0):
            try:
                x = values[pilha[0][0]]
            except:
                x = int(pilha[0][0])

            print(pilha)
            y += x

            try:
                for k in range((10 - x) + 1):
                    pilha.pop(0)
            except:
                continue

    pilha = mao + pilha

    print(pilha)

    print(f"case {i + 1}: {pilha[y - 1]}")

n = int(input())

for i in range(n):
    exercicio(i)