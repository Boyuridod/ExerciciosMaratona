N = int(input())

eels = []

for i in range(N):
    op = list(input().split(" "))

    peso = int(op[1])

    if(op[0] == "+"):
        eels.append(peso)

    else:
        eels.pop(eels.index(peso))

    # Teste

    i = 0
    j = 0

    tam = len(eels)

    danger = 0

    danger2 = 0

    teste = eels.copy()

    teste2 = eels.copy()

    while(i < tam):

        teste.sort()

        #print(teste)

        while(j < tam):
            
            #if(i != j):
            #    print(teste[i], teste[j])

            if(teste[i] >= teste[j] and i != j):

                if(teste[i] <= (2 * teste[j])):
                    danger += 1

                teste[i] += teste[j]

                teste.pop(j)

                teste.sort()

                j -= 1

                tam -= 1

                j = -1

                i = 0

            elif(teste[j] >= teste[i] and i != j):

                if(teste[j] <= (2 * teste[i])):
                    danger += 1

                teste[j] += teste[i]

                teste.pop(i)

                teste.sort()

                i -= 1

                tam -= 1

                j = -1

                i = 0

            j += 1

        i += 1
        j = 0

    print(danger)
