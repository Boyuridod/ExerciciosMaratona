N = int(input())

ant = 1
num = 1
aux = 0

for i in range(2,N):
    aux = num
    num = num + ant

    ant = aux

print(num)