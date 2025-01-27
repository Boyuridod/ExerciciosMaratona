lista = input().split(" ")

for i in range(len(lista)):
    lista[i] = int(lista[i])

lista.sort()

if(lista[2] < (lista[0] + lista[1])):
    print("S")

elif(lista[3] < (lista[1] + lista[2])):
    print("S")

else:
    print("N")