# https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/E

def crivo(n, ind):
    primos = [True] * (n + 1)

    primeiro = []

    primos[0] = False
    primos[1] = False

    for i in range(1, n + 1):
        if(primos[i]):
            primeiro.append(i)
            for j in range(i*i, n + 1, i):
                primos[j] = False

        if(len(primeiro) == ind):
            break

    return primeiro

ini, f, p = list(map(int, input().split(" ")))

primeiros = crivo(f, p)

dic = list(range(ini, f + 1))

for i in range(len(dic)):
    for j in primeiros:
        if(dic[i] % j == 0):
            dic[i] = 0
            break

print(sum(dic))