# https://codeforces.com/problemset/problem/1840/C

fats = {}

def fatorial(n):
    try:
        return fats[n]
    except:
        if(n == 0):
            fats[n] = 1
        else:
            for i in range(n):
                fats[n] = n * fatorial(n - 1)

    return fats[n]

def exercicio():
    n, k, q = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))

    dias = []
    aux = []

    for i in range(len(a)):
        if(a[i] <= q):
            aux.append(i + 1)
        else:
            if(len(aux) > 0):
                dias.append(aux)
                aux = []

    if(len(aux) > 0):
        dias.append(aux)
        aux = []

    op = 0

    for i in dias:
        if(len(i) > k):
            for j in range(len(i) - k + 2):
                op += j
        if(len(i) == k):
            op += 1

    return(int(op))

t = int(input())

while(t):
    print(exercicio())
    t -= 1