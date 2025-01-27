N = int(input())

qttDino = [0] * int(10e5)

for i in range(N):
    D, A = map(int, input().split(" "))

    D -= 1
    A -= 1
    
    for j in range(D, A + 1):
        qttDino[j] += 1

print(max(qttDino))
