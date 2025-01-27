import math

while(True):
    N, K = input().split(" ")
    N = int(N)
    K = int(K)

    if(N == 0 and K == 0):
        break

    elif(K > N or N == 0):
        print(0)

    elif(K == N):
        print(1)

    else:
        C = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

        print(C, end=" ")

        combinations = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

        print(combinations)