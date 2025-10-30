# https://codeforces.com/contest/2167/problem/D

from math import sqrt
from math import ceil

primos = {}
primos[0] = False
primos[1] = False

def ehPrimo(num):
    for i in range(2, num + 1):
        try:
            if(primos[i]):
                for j in range(i*i, num + 1, i):
                    primos[j] = False
        except:
            primos[i] = True
            for j in range(i*i, num + 1, i):
                primos[j] = False

ehPrimo(100)

def exercicio():
    tam = int(input())

    a = list(map(int, input().split(" ")))

    for i in range(len(primos)):
        ok = 0

        if(primos[i]):
            for j in a:
                if(j % i):
                    ok = 1
                    break

        if(ok):
            print(i)
            break

t = int(input())

for k in range(t):
    exercicio()