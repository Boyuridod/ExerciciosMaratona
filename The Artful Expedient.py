# https://vjudge.net/contest/746740#problem/I

n = int(input())
x = list(map(int, input().split(" ")))
y = list(map(int, input().split(" ")))

cont = 0

for i in range(len(x)):
    for j in range(len(y)):
        if(x[i] == y[j]):
            cont += 1
        elif(x[i] == x[j] and i != j):
            cont += 1
        elif(y[i] == y[j] and i != j):
            cont += 1

# print(help)

if(cont % 2 == 0):
    print("Karen")

else:
    print("Koyomi")