# https://open.kattis.com/contests/sfzh7d/problems/lineup

N = int(input())

nomes = []

increasing = False
decreasing = False

while(N > 0):
    nomes.append(input())

    N -= 1

for i in range(1, len(nomes)):
    if(nomes[i] > nomes[i - 1]):
        increasing = True
    elif(nomes[i] < nomes[i - 1]):
        decreasing = True

    if(increasing and decreasing):
        break

if(increasing and decreasing):
    print("NEITHER")
elif(increasing):
    print("INCREASING")
else:
    print("DECREASING")