mensagem = list(input())
crib = list(input())

cont = x = 0
y = len(crib)

for i in range(len(mensagem) - len(crib) + 1):
    certo = True
    for j in range(y):
        if(mensagem[i + j] == crib[j]):
            certo = False

        #print(mensagem[i + j], crib[j])

    if(certo):
        cont += 1

    #print("")
        
if(len(mensagem) == len(crib)):
    certo = True

    for i in range(len(mensagem)):
        if(mensagem[i] == crib[i]):
            certo = False

    if(certo):
        cont = 1


print(cont)