# https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/B

n = int(input())
ant = 1
antant = 1
j = 0

palavra = ["UAI", "TREM", "SO"]

i = 0

while(i < n):
    if(i == 0 or i == 1):
        print(ant, end=" ")
    else:
        fib = ant + antant

        if(len(str(fib)) != len(str(ant))):

            fib = ant + (10 ** (len(str(fib)) - 1))

            print(f"{palavra[j]}", end=" ")

            j += 1

            if(j == 3):
                j = 0

            antant = (10 ** (len(str(fib)) - 1))

            ant = fib

            if(i + 1 < n):
                print(fib, end=" ")

                n -= 1

        else:
            print(fib, end=" ")

            antant = ant

            ant = fib 

    i += 1

print("")