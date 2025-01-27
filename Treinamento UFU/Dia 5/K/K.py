N = int(input())
ami = []

def testa_num(num):
    lista = []
    for i in range(1, num + 1):
        if(num % i == 0):
            lista.append(i)

    return lista

for i in range(2,N + 1):
    ami.append(testa_num(i))

for i in ami:
    print(i)
