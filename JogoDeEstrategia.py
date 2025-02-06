J, R = input().split(" ")
J = int(J)
R = int(R)

rodadas = list(input().split(" "))
pontos = []
j = 0

for i in range(J * R):

    try:
        pontos[j] += int(rodadas[i])
    
    except:
        pontos.append(int(rodadas[i]))

    if(j >= J - 1):
        j = 0

    else:
        j += 1

maior = jogadr = 0

for i in range(J):
    if(pontos[i] >= maior):
        maior = pontos[i]
        jogador = i

print(jogador + 1)