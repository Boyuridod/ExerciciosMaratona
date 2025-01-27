N = int(input())

vogais = ['a','e','i','o','u']
trocar = ['@','&','!','*','%']

for i in range(N):
    frase = list(input())
    for j in range(len(frase)):
        if frase[j] in vogais:
            frase[j] = trocar[vogais.index(frase[j])]

    for j in frase:
        print(j,end=(""))

    print("")