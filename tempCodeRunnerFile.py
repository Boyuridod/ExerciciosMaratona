fats = {}

def fatorial(n):
    try:
        return fats[n]
    except:
        if(n == 0):
            fats[n] = 1
        else:
            for i in range(n):
                fats[n] = n * fatorial(n - 1)

    return fats[n]

print(fatorial(5))
print(fatorial(2))
print(fatorial(15))

print(fats)