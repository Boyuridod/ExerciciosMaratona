cartas = input().split(" ")

for i in range(len(cartas)):
    cartas[i] = int(cartas[i])

cartas.sort()

out = 0

for i in cartas:
    if(i == 1):
        out = "A"

    elif(i == 11):
        out = "J"

    elif(i == 12):
        out = "Q"

    elif(i == 13):
        out = "K"

    else:
        out = i

    print(out, end=" ")