# https://vjudge.net/problem/Kattis-rockpaperscissors

def exercicio(n, k):
    jogador = {}
    for i in range(1, n + 1):
        jogador[i] = [0, 0]

    for i in range(int((k * n * (n - 1)) / 2)):
        j1, m1, j2, m2 = input().split(" ")
        j1 = int(j1)
        j2 = int(j2)

        if(m1 != m2):
            jogador[j1][1] += 1
            jogador[j2][1] += 1

        if(m1 == "rock"):
            if(m2 == "paper"):
                jogador[j2][0] += 1
            elif(m2 == "scissors"):
                jogador[j1][0] += 1

        elif(m1 == "paper"):
            if(m1 == "scissors"):
                jogador[j2][0] += 1
            elif(m2 == "rock"):
                jogador[j1][0] += 1

        elif(m1 == "scissors"):
            if(m1 == "rock"):
                jogador[j2][0] += 1
            elif(m2 == "paper"):
                jogador[j1][0] += 1

    for i in jogador:
        try:
            print(f"{jogador[i][0]/ jogador[i][1]:.3f}")
        except:
            print("0.000")

    print("")

caso = list(map(int, input().split(" ")))

while(caso[0] != 0 and len(caso) != 1):

    exercicio(caso[0], caso[1])

    caso = list(map(int, input().split(" ")))