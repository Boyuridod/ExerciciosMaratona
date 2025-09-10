# https://vjudge.net/contest/746740#problem/B

import math

def exercicio():
    n, a, b, c = list(map(int, input().split(" ")))
    li = [a, b, c]

    skip = sum(li)

    dias = math.floor(n / skip)

    n -= dias * skip

    dias *= 3

    i = 0

    while(n > 0):
        n -= li[i]

        i += 1
        dias += 1

        if(i == 3):
            i = 0

    return dias
    

t = int(input())

while(t):
    print(exercicio())
    t -= 1