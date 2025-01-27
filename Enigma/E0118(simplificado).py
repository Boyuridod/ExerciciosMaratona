mensagem = list(input())
crib = list(input())

cont = 0
x = len(mensagem)
y = len(crib)

for i in range((x - y) + 1):
    certo = True

    for j in range(y):
        if(mensagem[i + j] == crib[j]):
            certo = False

    if(certo):
        cont += 1

print(cont)