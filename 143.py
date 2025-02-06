# https://neps.academy/br/exercise/143

tipos = [100, 50, 25, 10, 5, 1]
quantidade = [0]
aux = 0

C = int(input())

for i in tipos:
    aux = int(C / i)

    C -= i * aux

    quantidade[0] += aux
    quantidade.append(aux)

for i in quantidade:
    print(i)