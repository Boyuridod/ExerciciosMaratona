mod = 1e9 + 7

N = int(input())

res = 1

for i in range(N-1):
    res = (res * 2) % mod

print(int(res))