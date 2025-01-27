N = int(input())

for i in range(N):
    resultado = 0
    binario = list(input())

    binario.reverse()

    for j in range(len(binario)):
        resultado += int(binario[j]) * (2 ** j)

    print(resultado)