from math import ceil

def MDC(a, b):
    if(b == 0):
        return a
    return MDC(b, a%b)

def MMC(a, b):
    return a * b / MDC(a, b)

N = int(input())

paes = int(input())

cap = list(map(int, input().split(" ")))

mmc = cap[0]

for i in range(1, N - 1):
    mmc = MMC(mmc, cap[i])

somatorio = 0

for i in range(N):
    somatorio += mmc/cap[i]

t = ceil((paes * mmc)/somatorio)

print(t)