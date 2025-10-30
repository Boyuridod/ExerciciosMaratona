# https://codeforces.com/contest/2167/problem/C

def sorte(l):
    embaralhado = True

    while(embaralhado):
        embaralhado = False
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if(l[i] > l[j]):
                    if(l[i] & 1 != l[j] & 1):
                        aux = l[i]
                        l[i] = l[j]
                        l[j] = aux

                        embaralhado = True

                        j = i
                        i = len(l)

                        break

    return l

def exercicio():
    tam = int(input())

    brinq = list(map(int, input().split(" ")))

    ord = False

    prim = brinq[0] % 2

    for i in range(1, tam):
        if(prim != brinq[i] % 2):
            ord = True
            break

    if(ord):
        return sorted(brinq)
    
    else:
        return brinq

t = int(input())

for k in range(t):
    print(*exercicio())