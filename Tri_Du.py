cartas = input().split(" ")

carta = 0

for i in range(len(cartas)):
    cartas[i] = int(cartas[i])

if(cartas[0] == cartas[1]):
    carta = cartas[0]

elif(cartas[0] > cartas[1]):
    carta = cartas[0]

else:
    carta = cartas[1]

print(carta)