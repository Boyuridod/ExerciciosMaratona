N = int(input())

qttDino = [0] * 10

def arruma_dino(qttDino, a, b):

    if(a != b):
        qttDino[j] += 1
        return qttDino
    else:
        return qttDino

# for i in range(N):
try:
    D, A = map(int, input().split(" "))

    D -= 1
    A -= 1
    
    if(len(qttDino) < A):
        for j in range(len(qttDino), A + 1):
            qttDino.append(0)
    
    qttDino = arruma_dino(qttDino, D, A + 1)
except:
    print(max(qttDino))