N = int(input())

bilhar = []
sinuca = []

possivel = True

for i in range(N):
    x, y = input().split(" ")

    bilhar.append(int(x))

    sinuca.append(int(y))

# print(N/2, sum(bilhar), sum(sinuca))

lenth = len(bilhar)

if((sum(bilhar) % (N / 2) != 0 and sum(sinuca) % (N / 2) != 0) or N % 2 != 0):
    print("impossible")

    pontosBilhar = sum(bilhar) / (N / 2)
    pontosSinuca = sum(sinuca) / (N / 2)

    while(possivel and len(bilhar) > 0):
        x = bilhar[0]
        y = sinuca[0]
        lenth = len(bilhar)

        for i in range(0, lenth - 1):

            print("forzandi")

            if((x + bilhar[i]) == pontosBilhar and (y + sinuca[i]) == pontosSinuca and not possivel):
                possivel = True

                bilhar.pop(i)
                bilhar.pop(0)
 
                sinuca.pop(i)
                sinuca.pop(0)

                lenth -= 1

        print(possivel)

    if(possivel):
        print("possible")

    else:
        print("impossible")