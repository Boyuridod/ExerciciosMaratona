A, B = input().split(" ")
A = int(A)
B = int(B)

for i in range(A, B):
    isPrimo = True
    for j in range(2, int(i / 2) + 1):
        if(i % j == 0):
            isPrimo = False

            break

    if(isPrimo):

        print(i,end=" ")
