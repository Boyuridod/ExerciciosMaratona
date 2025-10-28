# https://codeforces.com/contest/2167/problem/C

def sorte(l):
    embaralhado = True

    while(embaralhado):
        embaralhado = False
        for i in range(len(l) - 1, -1, -1):
            for j in range(i, 0, -1):
                if(l[i] < l[j]):
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

    ret = ""

    for i in sorte(brinq):
        ret += f"{i} "

    return ret

t = int(input())

for k in range(t):
    print(exercicio())