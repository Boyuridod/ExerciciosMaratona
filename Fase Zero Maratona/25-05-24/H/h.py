import math

N = int(input())

def isPrimo(x):
    for j in range(2, int(math.sqrt(x))):
        if(x % j == 0):
            return False
        
    return True

for i in range(N):
    numero= int(input())
    
    if(numero == 3 or numero == 4):
        print(-1)

    elif(numero == 5):
        print(1, 4)

    else:
        for y in range(int(numero / 2), numero):
            if(not isPrimo(y) and not isPrimo(numero - y) and y != (numero - y)):
                print(numero - y, y)
                break
            elif(y == numero - 1):
                print(-1)