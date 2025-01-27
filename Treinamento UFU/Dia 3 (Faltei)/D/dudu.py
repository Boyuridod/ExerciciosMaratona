N = int(input())

aux = str(N)
cont = 0

while(aux != aux[::-1] and cont < 4):
    aux = list(aux)
    aux.reverse()

    num = 0

    for j in range(len(aux)):
        num += int(aux[j]) * (10 ** (len(aux) - j - 1))

    N += num

    aux = str(N)

    cont += 1

aux = str(N)

if(aux == aux[::-1]):
    print(N)

else:
    print("0")