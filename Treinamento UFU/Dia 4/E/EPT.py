import math

while True:
    N, K = map(int, input().split())

    if N == 0 and K == 0:
        break

    elif(K > N or N == 0):
        print(0)

    elif(K == N):
        print(1)

    else:

        combinations = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))

        print(combinations)