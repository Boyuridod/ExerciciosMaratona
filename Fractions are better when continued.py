# https://vjudge.net/contest/747064#problem/F

N = int(input())

antant = 0
ant = 1
fib = 1

for i in range(N):
    fib = ant + antant

    antant = ant

    ant = fib

print(fib)