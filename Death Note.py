# https://vjudge.net/contest/746740#problem/E

n, m = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))

amount = 0

for i in a:
    amount += i

    if(amount - m >= 0):
        print(int(amount / m), end=" ")
        amount -= int(amount / m) * m

    else:
        print(0, end=" ")

    # print(amount)

print("")