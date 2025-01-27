N = int(input())

qttDino = [0] * 10

while(True):
    try:
        D, A = map(int, input().split(" "))

        D -= 1
        A -= 1

        if(len(qttDino) < A):
            for j in range(len(qttDino), A + 1):
                qttDino.append(0)
        
        for j in range(D, A + 1):
            qttDino[j] += 1
    except:
        break

print(max(qttDino))