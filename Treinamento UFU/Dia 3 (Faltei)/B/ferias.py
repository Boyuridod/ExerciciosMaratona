N = int(input())

for i in range(N):
    T, I, A = input().split(" ")
    T = int(T)
    I = int(I)
    A = int(A)

    cont = 0

    while(T > 0):

        T -= I

        I += A

        cont += 1

    print(cont) 