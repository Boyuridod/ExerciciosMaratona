# https://codeforces.com/contest/2167/problem/A

def exercicio():
    a = list(map(int, input().split(" ")))

    for i in range(1, len(a)):
        if(a[0] != a[i]):
            return("NO")

    return "YES"

t = int(input())

for k in range(t):
    print(exercicio())