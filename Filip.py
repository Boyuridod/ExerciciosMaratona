# https://vjudge.net/problem/Kattis-filip

M, N = input().split(" ")

M = M[::-1]
N = N[::-1]

if(M > N):
    print(M)
else:
    print(N)