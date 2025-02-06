lista  = input().split(" ")

for i in range(len(lista)):
    lista[i] = int(lista[i])

lista.sort()

if(lista[0] - lista[1] == 0 or lista[0] - lista[2] == 0 or lista[1] - lista[2] == 0):
    print("S")

elif(lista[0] + lista[1] == lista[2]):
    print("S")

elif(0 in lista):
    print("S")

else:
    print("N")