# https://vjudge.net/contest/747064#problem/L

N = int(input())
a = list(map(int, input().split(" ")))

a.sort(reverse=True)
res = []

for i in range(N):
    a[i] &= sum(a) - a[i] - sum(res)
    res.append(a[i])
    a[i] = 0

print(*res)