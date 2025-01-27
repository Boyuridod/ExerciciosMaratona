N = int(input())

caramelos = list(map(int, input().split(" ")))

caramelos.sort(reverse=True)

A = []
B = []

for i in caramelos:
    if(sum(A) <= sum(B)):
        A.append(i)
    else:
        B.append(i)

contA = contB = 0

if(sum(A) == sum(B)):
    if(len(caramelos) % 2 == 0):
        A.sort()
        B.sort()

        for i in range(len(caramelos)):
            if(i % 2 == 0):
                print(A[contA], end=" ")
                contA += 1
            else:
                print(B[contB], end=" ")
                contB += 1

    else:
        # A.sort(reverse=True)
        # B.sort(reverse=True)

        print(B[0], end=" ")
        print(A[0], end=" ")
        A.pop(contA)
        B.pop(contB)

        while(contB + contA < len(caramelos) - 2):
            try:
                if(B[contB] >= A[contA]):
                    print(B[contB], end=" ")
                    contB += 1
                else:
                    print(A[contA], end=" ")
                    contA += 1
            except:
                print(A[-1], end=" ")
                contA += 1

else:
    print(-1)