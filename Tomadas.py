reguas = input().split(" ")

aparelhos = 0

for i in range(len(reguas)):
    aparelhos += int(reguas[i]) - 1

print(aparelhos + 1)