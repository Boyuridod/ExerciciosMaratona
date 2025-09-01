# https://vjudge.net/contest/744581#problem/B

tamanhos = {"S": -1, "M": 0, "L": 1, "X": 2}

def exercicio():
    x, y = input().split(" ")

    primeira = tamanhos[x[-1]]
    segunda = tamanhos[y[-1]]

    for i in x:
        if(i == "X"):
            primeira *= tamanhos[i]

    for i in y:
        if(i == "X"):
            segunda *= tamanhos[i]

    # print(primeira, segunda)

    if(primeira == segunda):
        print("=")

    elif(primeira > segunda):
        print(">")

    else:
        print("<")

n = int(input())

for asasas in range(n):
    exercicio()