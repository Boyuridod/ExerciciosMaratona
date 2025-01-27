N = int(input())

for i in range(N):
    num = int(input())
    x = 1

    for i in range(2, num//2):

        if(num % i == 0):
            x = 0
            break

    print(x)