# https://vjudge.net/contest/744581#problem

import math

x, y, z = list(map(int, input().split(" ")))

soma = math.sqrt(x) * 4
soma += math.sqrt(y) * 2
soma += math.sqrt(z) * 4

print(math.ceil(soma))