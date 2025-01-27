nome = input().split(" ")

proibido = ["da", "de", "do", "dos", "e"]

for i in range(len(nome)):
    if(i != 0 and i != (len(nome) - 1)):
        if(nome[i] not in proibido):
            nome[i] = nome[i][0] + "."
            print(nome[i], end=" ")

    elif(i == 0):
        print(nome[i], end=" ")

    else:
        print(nome[i])