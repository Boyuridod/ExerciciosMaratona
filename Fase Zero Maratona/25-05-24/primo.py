def isPrimo(x):
    for j in range(2, x):
        if(x % j == 0):
            return False
        
    return True

for i in range(500000000):

    if(isPrimo(i)):
        print(i,",", sep="", end=" ")