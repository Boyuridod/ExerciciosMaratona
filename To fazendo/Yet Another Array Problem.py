# https://codeforces.com/contest/2167/problem/D

from math import sqrt
from math import ceil

primos = {}
primos[0] = False
primos[1] = False

def ehPrimo(num):
    for i in range(num + 1):
        try:
            if(primos[i]):
                for j in range(i*i, num + 1):
                    primos[j] = False
        except:
            primos[i] = True

ehPrimo(100000)

def fatoresPrimos(num):
    fatores = []

    for i in range(2, ceil(sqrt(num)) + 1):
        if(num % i == 0 and primos[i]):
            fatores.append(i)
            while(num % i == 0):
                num /= i

    if(num > 1):
        fatores.append(int(num))

    return fatores

def exercicio():
    tam = int(input())

    a = list(map(int, input().split(" ")))

    menor = 10000000

    for i in a:
        fatores = fatoresPrimos(i)

        x = 2

        roda = True

        while(roda):
            roda = False

            for j in fatores:
                if(x % j == 0):
                    roda = True

                    x += 1

                    break

            if(x > menor):
                roda = False

        if(menor > x):
            menor = x

    return menor

t = int(input())

for k in range(t):
    print(exercicio())