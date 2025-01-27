N = int(input())

for i in range(N):
    A, B = input().split(" ")
    A = int(A)
    B = int(B)

    resto = 1

    while(resto != 0):
        resto = A % B

        A = B
        B = resto

    print(A)