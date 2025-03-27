# https://neps.academy/br/exercise/642

cont = 1
quantidade = 0

while(True):
    N = int(input())

    quantidade = 0

    if(N == -1):
        break

    else:
        if(cont != 1):
            print("\n\nTeste",cont)

        else:
            print("Teste",cont)

        quantidade = ((2 ** N) ** 2)

        cont += 1

        print(quantidade,end="")