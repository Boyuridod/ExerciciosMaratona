# https://open.kattis.com/contests/eqnk5p/problems/moscowdream

a, b, c, n = list(map(int, input().split(" ")))

if(a >= 1 and b >= 1 and c >= 1 and (a + b + c) >= n and n >= 3):
    print("YES")
else:
    print("NO")