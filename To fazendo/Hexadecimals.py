fib ={}

def fibonacci(n):
    if(n == 0):
        fib[n] = 0
    elif(n == 1):
        fib[n] = 1
    else:
        fib[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return fib[n]

n = int(input())

inde = 0

while(fibonacci(inde) < n):
    inde += 1

print(fib)

inde -= 1

cont = 3

nums = []

while(n > 0 and cont > 0 and inde >= 0):
    print(fib[inde], n)
    while(n >= fib[inde]):
        n -= fib[inde]

        nums.append(fib[inde])

        cont -= 1

    inde -= 1



print(nums)



if(cont == 0):
    for i in nums:
        print(i, end=" ")

    print("")

else:
    print("I'm too stupid to solve this problem")