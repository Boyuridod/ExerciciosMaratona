# https://neps.academy/br/exercise/25

N = int(input())

ganha = {
    1: [2, 3],
    2: [3, 4],
    3: [4, 0],
    4: [0, 1],
    0: [1, 2]
}

dario = 0
xerxes = 0

for i in range(N):
    d, x = list(map(int, input().split(" ")))
    
    if(x in ganha[d]):
        dario += 1
    else:
        xerxes += 1

if(dario > xerxes):
    print("dario")
else:
    print("xerxes")