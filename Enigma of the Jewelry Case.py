# https://vjudge.net/contest/747064#problem/E

N = int(input())

joias = []

for i in range(N):
    joias.append(list(map(int, input().split(" "))))

bordas = [joias[0][0], joias[0][N - 1], joias[N - 1][N - 1], joias[N - 1][0]]

print(bordas.index(min(bordas)))