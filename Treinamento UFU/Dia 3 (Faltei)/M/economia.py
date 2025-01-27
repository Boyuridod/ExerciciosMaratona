N = int(input())

total = 0
grana =  1

for i in range(0, N):
    total += 2 ** i

print(total)