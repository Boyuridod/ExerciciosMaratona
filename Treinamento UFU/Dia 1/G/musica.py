num = int(input())

frase = []

for i in range(num):
    frase.append(input())

for i in frase:
    if(i != frase[len(frase) - 1]):
        print(i,end=" ")
    else:
        print(i)